import csv

my_dialect = {
    'delimiter': '|',
    'lineterminator': '\n',
    'quoting': csv.QUOTE_MINIMAL
}

data = [
    {'car': 'BMW', 'color': 'grey', 'max speed': '10 km/h'},
    {'car': 'Audi', 'color': 'black', 'max speed': '11 km/h'}
]

with open('data.csv', 'w', newline='') as f:
    fieldnames = ['car', 'color', 'max speed']
    writer = csv.DictWriter(f, **my_dialect, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)