import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "
    csv_f.seek(0)  # zerujemy ponownie wskaźnik na element

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x00000247C55E7280>
    fields = next(csvreader)  # pobiera element i ustawia wskażnik na nastepny
    for row in csvreader:
        rows.append(row)

print(fields)
print(type(fields))  # <class 'list'>
print(rows)
# 11:15
