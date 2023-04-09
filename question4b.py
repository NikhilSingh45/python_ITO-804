def shift_left(lst):
    if len(lst) <= 1:
        return lst
    shifted_lst = lst[1:] + [lst[0]]
    return shifted_lst

# Sample list
sample_list = [1, 2, 3]

# Call the function to shift left
shifted_list = shift_left(sample_list)

# Print the original and shifted list
print("Original List:")
print(sample_list)
print("Shifted List:")
print(shifted_list)
