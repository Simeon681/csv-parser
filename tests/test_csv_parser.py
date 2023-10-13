import pytest
from app.csv_parser import CSVParser

FILE_PATH = "./data/example.csv"

@pytest.fixture
def parser():
    return CSVParser(FILE_PATH)

def test_count_rows(parser):
    assert parser.count_rows() == 4

def test_sum_column(parser):
    assert parser.sum_column("Age") == 118.0

def test_find_min(parser):
    assert parser.find_min("Age") == 25.0

def test_find_max(parser):
    assert parser.find_max("Age") == 35.0

def test_find_avg(parser):
    assert parser.find_avg("Age") == 29.5

def test_find_shortest_string(parser):
    assert parser.find_shortest_string("Name") == "Bob"

def test_find_longest_string(parser):
    assert parser.find_longest_string("City") == "San Francisco"
