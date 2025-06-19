from concurrent.futures import ThreadPoolExecutor as TPE
import time

start = time.time()

def fact(n):
    if n == 1:
        return n
    elif n > 1:
        return fact(n-1) * n

with TPE(max_workers=3) as exec:
    futures = [exec.submit(fact, i) for i in range(960, 965)]

for f in futures:
    print(f.result())

print(f'time: {time.time() - start}')