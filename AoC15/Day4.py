import re
import hashlib
import time

tic = time.perf_counter()
key = 'yzbqklnj'

int = 0
secretFound = False

while not secretFound:
    if re.search('^[0]{6}', (hashlib.md5((key + str(int)).encode())).hexdigest()):
        print(int)
        secretFound = True
    else:
        int += 1

toc = time.perf_counter()
print(f"Ran program in {toc - tic:0.4f} seconds")