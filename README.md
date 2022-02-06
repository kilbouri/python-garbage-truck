# python-garbage-truck

A rather simple Python bot with configurable garbage payload for filling scammer databases with meaningless information.

### Config

- `POST_TARGET`: a URL to post garbage to
- `THREAD_BATCH_SIZE`: the number of garbage entries each thread should attempt to post
- `NUM_THREADS`: the number of threads to create
- `generate_garbage()`: a function which generates the garbage data to post

### How to Run

1. Ensure you have the `requests` module: `pip3 install requests`
2. Configure everything in `main.py`
3. `python3 src/main.py`
4. Sit back and relax while the bot dumps a pile of garbage on the scammer's lawn
