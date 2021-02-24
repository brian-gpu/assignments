def find_numbers():
    results = []
    for num in range(1500, 2701):
        if num % 7 == 0 and num % 5 == 0:
            results.append(num)
    
    return results

print(find_numbers())