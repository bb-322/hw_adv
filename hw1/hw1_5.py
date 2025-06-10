import random

def gen_list():
    nums_list = []
    for i in range(random.randint(5, 15)):
        nums_list.append(random.randint(1,100))
    return nums_list

def main():
    result = []
    for num in gen_list():
        if num % 2 != 0:
            result.append(num**2)
    print(result)

main()