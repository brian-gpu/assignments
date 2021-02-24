def factorial(num):
    result = 1
    count = 0
    x1 = 0
    x2 = 0

    while(count < num + 1):
        if count == 0 or count == 1:
            result = 1
            x2 = result
        else:
            x1 = x2
            x2 = count
            result = x2 * x1
            x2 = result
        count += 1
    
    return result

num = int(input())
print(factorial(num))