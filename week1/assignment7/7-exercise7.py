def count_odd_even(numbers):
    total_odd = 0
    total_even = 0

    for num in numbers:
        if num % 2 == 1:
            total_odd += 1
        else:
            total_even += 1
    
    print(f"Number of even numbers : {total_even}")
    print(f"Number of odd numbers : {total_odd}")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd_even(numbers)