# Create a new list from two list using the following condition

def merge_lists(list1, list2):
    new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
    return new_list
