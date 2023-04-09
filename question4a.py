def remove_duplicates(lst_of_lsts):
    unique_lsts = []
    for lst in lst_of_lsts:
        if lst not in unique_lsts:
            unique_lsts.append(lst)
    return unique_lsts

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Call the function to remove duplicates
unique_list_of_lists = remove_duplicates(sample_list)

print("Original List of Lists:")
print(sample_list)
print("Unique List of Lists:")
print(unique_list_of_lists)
