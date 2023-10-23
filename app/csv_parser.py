import csv
import statistics

def parse_csv(file_path):
    data = []
    if not file_path.endswith('.csv'):
        raise ValueError("File should be .csv")
    elif not file_path:
        raise ValueError("File path should not be empty")  
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

class CSVParser:
    def __init__(self, data):
        self.data = data

    def count_rows(self):
        rows_len = len(self.data)

        assert rows_len == 3, "Rows length should not be greater or less than 3"
        assert rows_len != None, "Rows length should not be None"

        return rows_len
    
    def count_columns(self):
        columns_len = len(self.data[0].keys())

        assert columns_len == 3, "Columns length should not be greater or less than 3"
        assert columns_len != None, "Columns length should not be None"

        return columns_len
    
    def column_exists(self, column_name):
        if not column_name:
            raise ValueError("Column name should not be empty")
        for row in self.data:
            if column_name in row:
                return True
        return False
    
    def column_is_numeric(self, column_name):
        if not column_name:
            raise ValueError("Column name should not be empty") 
        for row in self.data:
            if row[column_name].strip():
                try:
                    float(row[column_name]) and float(row[column_name]) >= 0.0
                except ValueError:
                    return False
        return True

    def sum_column(self, column_name):
        if not column_name:
            raise ValueError("Column name should not be empty")
        total_sum = 0
        for row in self.data:
            try:
                total_sum += float(row[column_name])
            except ValueError:
                raise ValueError("Column should contain only numeric values")
        return total_sum

    def find_min(self, column_name):
        values = [float(row[column_name]) for row in self.data if row[column_name].strip()]
        minimum = min(values)
        
        assert minimum != None, "Minimum should not be None"

        return minimum

    def find_max(self, column_name):
        values = [float(row[column_name]) for row in self.data  if row[column_name].strip()]
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
