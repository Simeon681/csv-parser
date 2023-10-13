import csv
import statistics

class CSVParser:
    def __init__(self, file_path):
        self.data = self.parse_csv(file_path)

    def parse_csv(self, file_path):
        data = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)
        return data

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
        return min(values)

    def find_max(self, column_name):
        values = [float(row[column_name]) for row in self.data if row[column_name].strip()]
        return max(values)

    def find_avg(self, column_name):
        values = [float(row[column_name]) for row in self.data if row[column_name].strip()]
        return statistics.mean(values)

    def find_shortest_string(self, column_name):
        values = [row[column_name] for row in self.data if row[column_name].strip()]
        return min(values, key=len)

    def find_longest_string(self, column_name):
        values = [row[column_name] for row in self.data if row[column_name].strip()]
        return max(values, key=len)
