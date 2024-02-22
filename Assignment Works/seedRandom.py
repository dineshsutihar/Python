import random

def generate_random_numbers(seed=6):
    random.seed(seed)
    for _ in range(5):
        print(random.randint(10, 50))
import time

current_time = int(time.time())
generate_random_numbers(current_time)
