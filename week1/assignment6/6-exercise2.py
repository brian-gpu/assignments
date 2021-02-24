def crowd_test(crowd):
    if len(crowd) > 3:
        print('The room is crowded.')
    else:
        print('The room is not very crowded.')

print("Exercise 2")
# Crowd has 4 people
crowd = ['John','Dave','Sam','Sue']
crowd_test(crowd)

# Crowd has 3 people
crowd.remove('Dave')
crowd_test(crowd)