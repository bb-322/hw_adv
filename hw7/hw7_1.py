def func(list: list[int]) -> list[str]:
    for idx, value in enumerate(list):
        list[idx] = str(value)
    return list

mylist = [1, 2, 3, 4, 5, 6]

print(isinstance(mylist[0], int))
print(isinstance(mylist[0], str))

func(mylist)

print(isinstance(mylist[0], int))
print(isinstance(mylist[0], str))