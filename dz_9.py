import pytest

@pytest.fixture
def make_name_record():
    def _make_customer_record(name):
        return {"name": name}

    return _make_customer_record


def test_name_records(make_name_record):
    name_1 = make_name_record("John")
    name_2 = make_name_record("Name")
    name_3 = make_name_record("123")
