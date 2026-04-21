import random

def parse_logs():
    data = []

    # simulate log features
    for _ in range(100):
        packets = random.randint(1, 100)
        errors = random.randint(0, 10)
        data.append([packets, errors])

    return data
