import csv, os


class DataLoader:
    def __init__(self, folder=None):
        if folder is None:
            folder = os.path.dirname(os.path.realpath(__file__))
        self.folder = folder

    def load_csv(self, filename):
        path = os.path.join(self.folder, filename)
        with open(path) as f:
            rows = [dict(r) for r in csv.DictReader(f)]
        return Table(filename, rows)


class Table:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def convert(self, key, func):
        new_rows = [{**row, key: func(row[key])} for row in self.rows]
        return Table(self.name, new_rows)

    def filter(self, condition):
        return Table(self.name, [row for row in self.rows if condition(row)])

    def aggregate(self, key, aggregation_function):
        return aggregation_function([row[key] for row in self.rows])

    def __len__(self):
        return len(self.rows)

    def __iter__(self):
        return iter(self.rows)

    def __getitem__(self, index):
        return self.rows[index]

    def __str__(self):
        return f"Table '{self.name}' with {len(self)} rows"


average = lambda values: sum(values) / len(values)

if __name__ == "__main__":
    loader = DataLoader()
    cities = loader.load_csv('Cities.csv').convert('temperature', float)
    print(cities)
    print()

    # Print first 5 cities only
    for city in cities[:5]:
        print(city)
    print()

    # Print the average temperature of all the cities
    print("The average temperature of all the cities:")
    print(cities.aggregate('temperature', average))
    print()

    # Print all cities in Germany
    print("All cities in Germany:")
    for city in cities.filter(lambda c: c['country'] == 'Germany'):
        print(city)
    print()

    # Print all cities in Spain with a temperature above 12°C
    print("All cities in Spain with a temperature above 12°C:")
    warm_spain = cities.filter(
        lambda c: c['country'] == 'Spain' and c['temperature'] > 12)
    for city in warm_spain:
        print(city)
    print()

    # Count the number of unique countries
    print("The number of unique countries:")
    print(cities.aggregate('country', lambda names: len(set(names))))
    print()

    # Print the average temperature for all the cities in Germany
    print("The average temperature for all the cities in Germany:")
    german_cities = cities.filter(lambda c: c['country'] == 'Germany')
    print(german_cities.aggregate('temperature', average))
    print()

    # Print the max temperature for all the cities in Italy
    print("The max temperature for all the cities in Italy:")
    italian_cities = cities.filter(lambda c: c['country'] == 'Italy')
    print(italian_cities.aggregate('temperature', max))