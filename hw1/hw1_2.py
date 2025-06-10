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
def test_func():
    for i in range(1000):
        print(i)

@get_time
def test2_func(num1, num2):
    for i in range(num1, num2+1):
        print(i)

test_func()
test2_func(169, 82123)