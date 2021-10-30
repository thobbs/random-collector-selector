#!/bin/env/python3

import random
import time

current_time = time.time()
current_time_formatted = time.ctime(current_time)
print(f"current time: {current_time_formatted} CDT")
print(f"seconds since epoch: {current_time}")

seed = int(current_time * 1000)
print(f"seed: {seed}")

random.seed(seed)

candidates = list(range(0, 999))
random.shuffle(candidates)

print("")
print("Selected Candidates")
print("-------------------")
for i, candidate in enumerate(candidates[:24], 1):
    print(f"{i:2d}: Fidenza {candidate:3d}")

print("")
print("Backup Candidates")
print("-----------------")
for i, candidate in enumerate(candidates[24:55], 25):
    print(f"{i:2d}: Fidenza {candidate:3d}")
