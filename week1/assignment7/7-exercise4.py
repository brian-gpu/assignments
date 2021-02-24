def create_pattern():
    symbols = 1

    for row in range(0,9):
        for col in range(0, symbols):
            print("* ", end='')

        if row < 4:
            symbols += 1
        else:
            symbols -= 1
            
        print("")

create_pattern()