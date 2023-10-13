from app.csv_parser import CSVParser

file_path = "example.csv"
parser = CSVParser(file_path)

print("Number of rows:", parser.count_rows())
print("Sum of a column:", parser.sum_column("Age"))
print("Minimum in a column:", parser.find_min("Age"))
print("Maximum in a column:", parser.find_max("Age"))
print("Average in a column:", parser.find_avg("Age"))
print("Shortest string in a column:", parser.find_shortest_string("Name"))
print("Longest string in a column:", parser.find_longest_string("City"))