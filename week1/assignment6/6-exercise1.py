def crowd_test(crowd):
    if len(crowd) > 3:
        print('The room is crowded.')

print("Exercise 1")
# Crowd has 4 people
crowd = ['John','Dave','Sam','Sue']
crowd_test(crowd)

# Crowd has 3 people
crowd.remove('Dave')
crowd_test(crowd)