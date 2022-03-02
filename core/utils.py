from collections import Counter

import numpy as np


def find_color(number: int):
    a = ['Blue', 'Green', 'Red']
    result = np.random.choice(a, 100, p=[0.55, 0.30, 0.15])

    red = np.count_nonzero(result == 'Red')
    green = np.count_nonzero(result == 'Green')
    blue = np.count_nonzero(result == 'Blue')
    b = [red, green, blue]

    freq = Counter(result).most_common(3)

    attempts = []
    count = 0

    for t in freq:
        for color in t:
            if type(color) is int:
                break
            else:
                if result[number] == color:
                    count += 1
                    attempts.append(f"You're right, it`s {color}. Attempts = {count}")
                    return " \n ".join(attempts), color
                else:
                    count += 1
                    attempts.append(f"You're not right, it's not {color}. Attempts = {count}")

    return " \n ".join(attempts)
