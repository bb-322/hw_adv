import functools
import time

def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(end_time)
        return result
    return wrapper

@get_time
def fibo():
    nums = [1,1]
    for _ in range(1000-len(nums)):
        new_num = nums[-1] + nums[-2]
        nums.append(new_num)
    print(nums)

@get_time
@functools.lru_cache(10)
def fibo_cache10():
    nums = [1,1]
    for _ in range(1000-len(nums)):
        new_num = nums[-1] + nums[-2]
        nums.append(new_num)
    print(nums)

@get_time
@functools.lru_cache(16)
def fibo_cache16():
    nums = [1,1]
    for _ in range(1000-len(nums)):
        new_num = nums[-1] + nums[-2]
        nums.append(new_num)
    print(nums)

fibo()
fibo_cache10()
fibo_cache16()