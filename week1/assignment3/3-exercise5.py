import re

def is_palindrome(value):
    value = re.sub(r'[^a-z]','',value.lower())
    N = len(value)

    for index in range(0, N):
        if value[index] != value[(-index)-1]:
            return False

    return True

def collect_phrases(number_of_phrases):
    phrases = []
    index = 0

    while index < number_of_phrases:
        phrases.append(input())
        index += 1

    return phrases

def check_phrases(phrases):
    results = ""
    for p in phrases:
        if(is_palindrome(p)):
            results += "Y "
        else:
            results += "N "
            
    return results

number_of_phrases = int(input('Input data:\n'))
phrases = collect_phrases(number_of_phrases)
results = check_phrases(phrases)

print('\nanswer:')
print(results)