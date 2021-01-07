import time
import random


def really_slow_method(a, b):
    time.sleep(1)
    return random.choice([a, b])


if (result := really_slow_method(3, 4)) > 3:
    print(f"Passed with result: {result}")
else:
    print(f"Failed with result: {result}")
