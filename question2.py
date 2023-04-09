def find_earliest_trilogy_year(titles, years):
    earliest_year = None
    # Sort the years list in ascending order
    sorted_years = sorted(years)

    for i in range(len(sorted_years) - 2):
        # Check if the current year and the next two years form a trilogy
        if sorted_years[i] + 1 == sorted_years[i + 1] and sorted_years[i + 1] + 1 == sorted_years[i + 2]:
            earliest_year = sorted_years[i]
            break
    return earliest_year
