import string
import random


def generate_short_url():
    """Generates a random 8-character base62 string."""
    alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase
    random_base62 = ''.join(random.choice(alphabet) for _ in range(8))
    print(random_base62)


generate_short_url()
