from random import choice, randrange
from string import ascii_letters, digits

email_domains = [
    "yahoo.com",
    "gmail.com",
    "outlook.com",
    "hotmail.com",
    "live.com",
    "yahoo.co.uk",
    "gmail.co.uk",
    "outlook.co.uk",
    "hotmail.co.uk",
    "live.co.uk",
    "aol.com"
]


def random_string(length: int, numbers: bool = False):
    if numbers:
        def gen(): return choice(digits + ascii_letters + digits)
    else:
        def gen(): return choice(ascii_letters)

    return "".join([gen() for _ in range(length)])


def random_email(minLen: int = 4, maxLen: int = 30):
    unameLen = randrange(minLen, maxLen)
    return random_string(unameLen, True) + "@" + choice(email_domains)


def random_credentials(unameLen: tuple = (4, 30), passLen: tuple = (8, 32)):
    passLen = randrange(*passLen)
    return (random_email(*unameLen), random_string(passLen))
