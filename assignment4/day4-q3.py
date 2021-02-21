def generate_dictionary(n):
    results = {}
    for num in range(1, n + 1):
        results[num] = num*num
    
    return results

n = int(input())
dictionary = generate_dictionary(n)
print(dictionary)