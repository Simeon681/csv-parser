import pytest
import csv
from app.csv_parser import CSVParser, parse_csv

#FILE_PATH = "./data/example.csv"

CSV_DATA = """Name,City,Age
Simeon,Sofia,25
Viktor,Plovdiv,35
Bobi,Veliko Tarnovo,39
"""

@pytest.fixture
def mock_open(mocker):
    mocker_open_csv = mocker.mock_open(read_data=CSV_DATA)
    mocker.side_effect = csv.Error("File is not a valid CSV file")
    mocker.patch("builtins.open", mocker_open_csv)

def test_parse_csv_with_fixture(mocker, mock_open):
    data = parse_csv('file_path.csv')
    expected_data = [
        {'Name': 'Simeon', 'City': 'Sofia', 'Age': '25'},
        {'Name': 'Viktor', 'City': 'Plovdiv', 'Age': '35'},
        {'Name': 'Bobi', 'City': 'Veliko Tarnovo', 'Age': '39'}
    ]

    assert data == expected_data

@pytest.fixture
def parser(mocker, mock_open):
    return CSVParser(parse_csv('file_path.csv'))

def test_count_rows(parser):
    assert parser.count_rows() == 3

def test_count_columns(parser):
    assert parser.count_columns() == 3

def test_column_exists(parser):
    assert parser.column_exists("Name") == True
    assert parser.column_exists("Age") == True
    assert parser.column_exists("City") == True
    assert parser.column_exists("Not existing column") == False

def column_is_numeric(parser):
    assert parser.column_is_numeric("Name") == False
    assert parser.column_is_numeric("Age") == True
    assert parser.column_is_numeric("City") == False

def test_sum_column_throws_exception(parser):
    with pytest.raises(ValueError) as e:
        parser.sum_column("Name")

    assert e.type == ValueError

def test_sum_column(parser):
    assert parser.sum_column("Age") == 99.0

def test_find_min(parser):
    assert parser.find_min("Age") == 25.0

def test_find_max(parser):
    assert parser.find_max("Age") == 39.0

def test_find_avg(parser):
    assert parser.find_avg("Age") == 33.0

def test_find_shortest_string(parser):
    assert parser.find_shortest_string("Name") == "Bobi"

def test_find_longest_string(parser):
    assert parser.find_longest_string("City") == "Veliko Tarnovo"
