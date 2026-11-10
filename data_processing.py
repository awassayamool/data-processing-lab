import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        row = dict(r)
        row['temperature'] = float(row['temperature'])
        cities.append(row)


def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    return aggregation_function([item[aggregation_key] for item in dict_list])


average = lambda values: sum(values) / len(values)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature', average, cities))
print()

# Print all cities in Germany
print("All cities in Germany:")
for city in filter_items(lambda c: c['country'] == 'Germany', cities):
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
warm_spain = filter_items(
    lambda c: c['country'] == 'Spain' and c['temperature'] > 12, cities)
for city in warm_spain:
    print(city)
print()

# Count the number of unique countries
print("The number of unique countries:")
print(aggregate('country', lambda names: len(set(names)), cities))
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
german_cities = filter_items(lambda c: c['country'] == 'Germany', cities)
print(aggregate('temperature', average, german_cities))
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
italian_cities = filter_items(lambda c: c['country'] == 'Italy', cities)
print(aggregate('temperature', max, italian_cities))
