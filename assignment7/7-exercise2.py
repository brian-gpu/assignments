def convert_temperature(temperature):
    old_temperature = temperature
    new_temperature = 0

    if(old_temperature[-1] == 'F'):
        new_temperature = float(old_temperature[0:-2])
        new_temperature -= 32
        new_temperature *= (5/9)
        new_temperature = int(new_temperature)

        print(f"{old_temperature} is {new_temperature} in Celsius")
    else:
        new_temperature = float(old_temperature[0:-2])
        new_temperature *= (9/5)
        new_temperature += 32
        new_temperature = int(new_temperature)

        print(f"{old_temperature} is {new_temperature} in Fahrenheit")

temperature = input("Input a temperature:\n")
convert_temperature(temperature)