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
# Example usage
titles = ['The Hunger Games', 'Catching Fire', 'Mockingjay', 'The Lord of the Rings', 'The Two Towers', 'The Return of the King', 'Divergent', 'Insurgent', 'Allegiant']
years = [2008, 2009, 2010, 1954, 1955, 1956, 2011, 2012, 2013]
earliest_year = find_earliest_trilogy_year(titles, years)
if earliest_year:
    print("The earliest year in which a trilogy was published is:", earliest_year)
else:
    print("No trilogy was found in the given list of books and years.")

