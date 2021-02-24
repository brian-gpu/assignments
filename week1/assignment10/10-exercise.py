def check_samples(samples):
    results = ''
    bmis = list(map(lambda s: s[0] / (s[1] ** 2), samples))
    levels = list(map(lambda b: 
                        (b < 18.5) * "under " or
                        ((b >= 18.5) and (b < 25.0)) * "normal " or
                        ((b >= 25.0) and (b < 30.0)) * "over " or
                        (b >= 30.0) * "obese ", bmis))
    
    return results.join(map(str, levels))


number_of_samples = int(input('input data:\n'))
samples = []
count = 0

while count < number_of_samples:
    s = input().split(' ')
    samples.append([float(s[0]), float(s[1])])
    count += 1

print('\nanswer:')
print(check_samples(samples))
