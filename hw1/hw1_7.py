from functools import partial
def mult(num1, num2):
    return num1 * num2

mult = lambda num1, num2: num1 * num2
mult_by_2 = partial(mult, 2)

print(mult_by_2(2))
print(mult_by_2(2, 4)) # doesnt work