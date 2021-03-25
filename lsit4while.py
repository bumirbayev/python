# Problem 2
# Write a function that prints each element in the list on a separate line

"""
def print_list(lst):
    i = 0
    while i < len(lst):
        print(lst[i])

"""
# if you will print_list[3, 4, 5], it will display all 3-s
"""
def list_numbers(n):
    i = 0
    new_list = []
    while i <= n:
        new_list.append(i)
        i += 1

    return 5

"""
def list_numbers(n):
    i = 0
    new_list = []
    while i <= n:
        if i % 2 == 0:
            new_list.append(i)
        i += 1

    return new_list

# list_numbers(10) will print [0, 2, 4, 6, 8, 10]
