def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Original list
original_list = [11, 45, 8, 11, 23, 45, 23, 45, 89, 11, 89]

# Call the function to count occurrences
occurrence_dict = count_occurrences(original_list)

# Print the original list and the occurrence dictionary
print("Original List:")
print(original_list)
print("Occurrence Dictionary:")
print(occurrence_dict)
