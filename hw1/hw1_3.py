import functools



# def fibo(num):
#     if num == 1 or num == 2:
#         return 1
#     if num > 2:
#         return (fibo(num - 1) + fibo(num - 2))


# @functools.lru_cache(10)
# def fibo_cache10(num):
#     if num == 1 or num == 2:
#         return 1
#     if num > 2:
#         return (fibo(num - 1) + fibo(num - 2))


# @functools.lru_cache(16)
# def fibo_cache16(num):
#     if num == 1 or num == 2:
#         return 1
#     if num > 2:
#         return (fibo(num - 1) + fibo(num - 2))

# print(fibo(25))
# print(fibo_cache10(25))
# print(fibo_cache16(25))



def fibo():
    nums = [1,1]
    for _ in range(1000-len(nums)):
        new_num = nums[-1] + nums[-2]
        nums.append(new_num)
    print(nums)


@functools.lru_cache(10)
def fibo_cache10():
    nums = [1,1]
    for _ in range(1000-len(nums)):
        new_num = nums[-1] + nums[-2]
        nums.append(new_num)
    print(nums)


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