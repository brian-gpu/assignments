def count_and_skip():
    results = ""
    for num in range(0, 7):
        if num == 3 or num == 6:
            continue
        else:
            results += str(num) + " "
    
    return results

print(count_and_skip())