import os
import random
import timeit

# print("Making file")
# with open('huge.txt', 'w') as f:
#     target_size = 50 * 1024 * 1042
#     while os.stat('huge.txt').st_size < target_size:
#         f.write(random.randint(0, 1000000).__str__() + "\n")
# print("Finished making file")


setup = """
num = 0
with open('huge.txt', 'r') as f:
    text = f.readlines()
    for line in text:
        if line.strip().isdigit():
            num += int(line.strip())
"""

print(timeit.timeit(setup, number=10))

setup = """
num = 0
with open('huge.txt', 'r') as f:
    for line in f:
        if line.strip().isdigit():
            num += int(line.strip())
"""

print(timeit.timeit(setup, number=10))


setup = """
num = 0
with open('huge.txt', 'r') as f:
    x = (int(line.strip()) for line in f if line.strip().isdigit())
    num = sum(x)
"""

print(timeit.timeit(setup, number=10))




