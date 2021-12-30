import pytest
from src.dummy_package.date_parser import date_parser

def test_always_true():
    """Simple pytest check"""
    assert True


@pytest.mark.parametrize('date, parsed_date', [
    ("20211201", ["20211201"]),
    ("20211201-20211203", ["20211203", "20211202", "20211201"]),
    ("20211201-20211203,20211202", ["20211203", "20211202", "20211201"])
])
def test_return_length(date, parsed_date):
    assert date_parser(date) == parsed_date
