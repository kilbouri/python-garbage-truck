from multiprocessing import Lock
from threading import Thread
from garbage_generator import random_credentials
from requests import post

#
# CONFIG SECTION ==============================================================
#

# The URL to post garbage data to
POST_TARGET = "https://a.bad.actor.com"

# how many posts should each thread make?
THREAD_BATCH_SIZE = 10

# how many threads total do you want?
NUM_THREADS = 5


def generate_garbage():
    # modify this function to change the data sent to the bad actor
    email, password = random_credentials()
    return {
        'email': email,
        'password': password
    }


#
# DRIVER CODE SECTION =========================================================
#

print_lock = Lock()


def threaded_print(string: str):
    print_lock.acquire()
    print(string)
    print_lock.release()


def post_garbage():
    garbage = generate_garbage()
    try:
        res = post(POST_TARGET, allow_redirects=True, data=garbage)
    except:
        threaded_print("POST failure")
        return

    ok = "OK" if res.ok else "FAILURE"
    threaded_print(f"POSTED [{garbage}]: {ok} - {res.status_code}")


def thread_target():
    for _ in range(THREAD_BATCH_SIZE):
        post_garbage()


def main():
    threads = []

    # Create NUM_THREADS daemon threads targeting thread_target
    print(f"Preparing {NUM_THREADS} threads...")
    for i in range(NUM_THREADS):
        threads.append(
            Thread(name=f"Spambot Thread #{i}", daemon=True, target=thread_target)
        )

    # Start all threads
    print(f"Starting threads...")
    for thread in threads:
        thread.start()

    # Join all threads (wait for completion)
    print(f"Awaiting thread completion...")
    for thread in threads:
        thread.join()

    print(f"Threads finished")


if __name__ == "__main__":
    main()
