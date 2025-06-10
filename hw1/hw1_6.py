# def get_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time() - start_time
#         print(end_time)
#         return result
#     return wrapper


def evens(func):
    def wrapper(n, *args, **kwargs):
        even_nums = []
        nums = func(n, *args, **kwargs)
        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
        print(even_nums)
        return nums
    return wrapper

@evens
def fibo_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibo_gen(25)
