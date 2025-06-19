import threading
import time

start = time.time()

def fact(n, result_h, index):
    if n == 1:
        result = 1
    elif n > 1:
        result = fact(n-1, result_h, index) * n
    
    result_h[index] = result
    return result

result = [None]

for i in range(960, 965):
    t = threading.Thread(target=fact, args=(i, result, 0,))
    t.start()
    t.join()
    print(result[0])

print(f'time: {time.time() - start}')