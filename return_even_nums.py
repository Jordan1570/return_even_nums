# Write a Python program to print the even numbers from a given list.

def print_even_nums(list_of_nums):

    for num in list_of_nums:
        if num % 2 == 0:
            print(num)

print_even_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])