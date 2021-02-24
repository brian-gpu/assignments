def find_numbers():
    results = ""
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            results += str(num) + ", "
    
    results = results[:-2]
    return results

results = find_numbers()
print(results)