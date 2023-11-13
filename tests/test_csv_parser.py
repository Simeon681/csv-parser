import pytest
import csv
from statistics import StatisticsError
from app.csv_parser import CSVParser, parse_csv
# FILE_PATH = "./data/example.csv"

CSV_DATA = """Name,City,Age
Simeon,Sofia,25
Viktor,Plovdiv,35
Bobi,Veliko Tarnovo,39
"""

INVALID_AGE = [
    {"Name": "Simeon", "City": "Sofia", "Age": ""},
    {"Name": "Viktor", "City": "Plovdiv", "Age": ""},
    {"Name": "Bobi", "City": "Veliko Tarnovo", "Age": ""},
]

INVALID_STRINGS = [
    {"Name": "", "City": "", "Age": "25"},
    {"Name": "", "City": "", "Age": "35"},
    {"Name": "", "City": "", "Age": "39"},
]


@pytest.fixture
def mock_open(mocker):
    mocker_open_csv = mocker.mock_open(read_data=CSV_DATA)
    mocker.side_effect = csv.Error("File is not a valid CSV file")
    mocker.patch("builtins.open", mocker_open_csv)


def test_parse_csv_with_fixture(mocker, mock_open):
    data = parse_csv("file_path.csv")
    expected_data = [
        {"Name": "Simeon", "City": "Sofia", "Age": "25"},
        {"Name": "Viktor", "City": "Plovdiv", "Age": "35"},
        {"Name": "Bobi", "City": "Veliko Tarnovo", "Age": "39"},
    ]

    assert data == expected_data


@pytest.fixture
def parser(mocker, mock_open):
    return CSVParser(parse_csv("file_path.csv"))


def test_parse_csv_with_invalid_file():
    with pytest.raises(ValueError) as e:
        parse_csv("file_path.txt")

    assert e.type == ValueError


def test_parse_csv_with_empty_file():
    with pytest.raises(ValueError) as e:
        parse_csv("")

    assert e.type == ValueError


def test_count_rows(parser):
    assert parser.count_rows() == 3


def test_count_rows_throws_exception(parser):
    parser.data = [
        {"Name": "Simeon", "City": "Sofia", "Age": "25"},
        {"Name": "Viktor", "City": "Plovdiv", "Age": "35"},
    ]
    with pytest.raises(AssertionError) as e:
        parser.count_rows()

    assert e.type == AssertionError


def test_count_columns(parser):
    assert parser.count_columns() == 3


def test_count_columns_throws_exception(parser):
    parser.data = [
        {"Name": "Simeon", "Age": "25"},
        {"Name": "Viktor", "Age": "35"},
        {"Name": "Bobi", "Age": "39"},
    ]
    with pytest.raises(AssertionError) as e:
        parser.count_columns()

    assert e.type == AssertionError


def test_column_exists(parser):
    assert parser.column_exists("Name") is True
    assert parser.column_exists("Age") is True
    assert parser.column_exists("City") is True
    assert parser.column_exists("Country") is False


def test_column_exists_with_empty_column_name(parser):
    with pytest.raises(ValueError) as e:
        parser.column_exists("")

    assert e.type == ValueError


def test_column_is_numeric(parser, benchmark):
    result = benchmark(parser.column_is_numeric, "Age")
    assert result is True


def test_column_is_numeric_with_empty_column_name(parser):
    with pytest.raises(ValueError) as e:
        parser.column_is_numeric("")

    assert e.type == ValueError


def test_sum_column(parser, benchmark):
    result = benchmark(parser.sum_column, "Age")
    assert result == 99.0


def test_sum_column_with_empty_column_name(parser):
    with pytest.raises(ValueError) as e:
        parser.sum_column("")

    assert e.type == ValueError


def test_sum_column_throws_exception(parser):
    with pytest.raises(ValueError) as e:
        parser.sum_column("Name")
        parser.sum_column("City")

    assert e.type == ValueError


def test_find_min(parser, benchmark):
    result = benchmark(parser.find_min, "Age")
    assert result == 25.0


def test_find_max(parser):
    assert parser.find_max("Age") == 39.0


def test_find_avg(parser):
    assert parser.find_avg("Age") == 33.0


def test_find_min_throws_exception(parser):
    with pytest.raises(ValueError) as e:
        parser.find_min("City")

    assert e.type == ValueError


def test_find_max_throws_exception(parser):
    with pytest.raises(ValueError) as e:
        parser.find_max("City")

    assert e.type == ValueError


def test_find_avg_throws_exception(parser):
    with pytest.raises(ValueError) as e:
        parser.find_avg("Name")

    assert e.type == ValueError


def test_find_min_with_empty_values(parser):
    parser.data = INVALID_AGE
    with pytest.raises(ValueError) as e:
        parser.find_min("Age")

    assert e.type == ValueError


def test_find_max_with_empty_values(parser):
    parser.data = INVALID_AGE
    with pytest.raises(ValueError) as e:
        parser.find_max("Age")

    assert e.type == ValueError


def test_find_avg_with_empty_values(parser):
    parser.data = INVALID_AGE
    with pytest.raises(StatisticsError) as e:
        parser.find_avg("Age")

    assert e.type == StatisticsError


def test_find_shortest_string(parser):
    assert parser.find_shortest_string("Name") == "Bobi"


def test_find_longest_string(parser):
    assert parser.find_longest_string("City") == "Veliko Tarnovo"


def test_find_shortest_string_with_empty_values(parser):
    parser.data = INVALID_STRINGS
    with pytest.raises(ValueError) as e:
        parser.find_shortest_string("Name")

    assert e.type == ValueError


def test_find_longest_string_with_empty_values(parser):
    parser.data = INVALID_STRINGS
    with pytest.raises(ValueError) as e:
        parser.find_longest_string("Name")

    assert e.type == ValueError
