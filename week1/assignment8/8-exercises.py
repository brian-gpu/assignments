import re

def func():
    print("Hello World")

def func1(name):
    print(f"Hi My name is {name}")

def func3(x, y, z):
    if z:
        return x
    else:
        return y

def func4(x=0, y=0):
    return x*y

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_greater_than(x, y):
    if x > y:
        return True
    else:
        return False

def sum_args(*args):
    return sum(args)

# Assumption: args are integers that are even or odd
def get_even_args(*args):
    results = []

    for a in args:
        if a % 2 == 0:
            results.append(a)
    
    return results

# Assumption: a letter is odd or even due to its
# position in the string
def lower_and_cap(data):
    results = ""
    n = len(data)
    for index in range(0, n):
        if index % 2 == 0:
            results += (data[index]).upper()
        else:
            results += (data[index]).lower()
    
    return results 

def find_number(x, y):
    result = 0
    if x % 2 == 0 and y % 2 == 0:
        result = min(x, y) - 1
    else:
        result = max(x, y) + 1

    return result

def func11(x, y):
    if len(x) == 0 and len(y) == 0:
        return True
    elif len(x) == 0 or len(y) == 0:
        return False
    elif x[0].lower() == y[0].lower():
        return True
    else:
        return False

def func12(x):
    result = 0
    target = 7
    distance = abs(x - target)

    if x < target:
        result = target + (2*distance)
    else:
        result = target - (2*distance)
    
    return result

def func13(x):
    result = ""
    sentence = x.split(' ')

    for word in sentence:
        w = ""
        for index in range(0, len(word)):
            if index == 0 or index == 3:
                w += word[index].upper()
            else:
                w += word[index]

        result += w + " "

    return result

print("Exercise 1:")
func()
print("Exercise 2:")
func1("Google")
print("Exercise 3:")
print(func3('Hello','Goodbye',False))
print("Exercise 4:")
print(func4(5,2))
print("Exercise 5:")
print(is_even(4))
print("Exercise 6:")
print(is_greater_than(2,3))
print("Exercise 7:")
print(sum_args(1,2,3,4,5))
print("Exercise 8:")
print(get_even_args(1,4,5,6,8))
print("Exercise 9:")
print(lower_and_cap("Hello World"))
print("Exercise 10:")
print(find_number(2,5))
print("Exercise 11:")
print(func11('sample','Star'))
print("Exercise 12:")
print(func12(3))
print("Exercise 13:")
print(func13("Hello World!"))