import csv
import statistics

def parse_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

class CSVParser:
    def __init__(self, data):
        self.data = data

    def count_rows(self):
        return len(self.data)

    def sum_column(self, column_name):
        total_sum = 0
        for row in self.data:
            try:
                total_sum += float(row[column_name])
            except ValueError:
                pass
        return total_sum

    def find_min(self, column_name):
        values = [float(row[column_name]) for row in self.data if row[column_name].strip()]
        minimum = min(values)
        
        assert minimum != None, "Minimum should not be None"

        return minimum

    def find_max(self, column_name):
        values = [float(row[column_name]) for row in self.data if row[column_name].strip()]
        maximum = max(values)

        assert maximum != None, "Maximum should not be None"

        return maximum

    def find_avg(self, column_name):
        values = [float(row[column_name]) for row in self.data if row[column_name].strip()]
        avg = statistics.mean(values)

        assert avg != None, "Average should not be None"

        return avg

    def find_shortest_string(self, column_name):
        values = [row[column_name] for row in self.data if row[column_name].strip()]
        shortest_string = min(values, key=len)

        assert shortest_string != None, "Shortest string should not be None"

        return shortest_string

    def find_longest_string(self, column_name):
        values = [row[column_name] for row in self.data if row[column_name].strip()]
        longest_strng = max(values, key=len)

        assert longest_strng != None, "Longest string should not be None"

        return longest_strng
