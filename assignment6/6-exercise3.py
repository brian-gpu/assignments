def crowd_test(crowd):
    crowd_size = len(crowd)

    if crowd_size > 5:
        print('There is a mob in the room')
    elif crowd_size > 2 and crowd_size < 6:
        print('The room is crowded.')
    elif crowd_size > 0 and crowd_size < 3:
        print('The room is not crowded.')
    else:
        print('The room is empty.')

print("Exercise 3")
# Crowd has 6 people
crowd = ['John','Dave','Sam','Sue','Jane','Tom']
crowd_test(crowd)

# Crowd has 4 people
crowd.pop(0)
crowd.pop(0)
crowd_test(crowd)

# Crowd has 2 people
crowd.pop(0)
crowd.pop(0)
crowd_test(crowd)

# Crowd has 0 people
crowd.pop(0)
crowd.pop(0)
crowd_test(crowd)