from dz_9 import make_name_record

def test_name_records():
    name_1 = make_name_record("John")
    name_2 = make_name_record("Name")

def test_name_records_by_string(name):
    print(name)
    if isinstance(name, str):
        make_name_record(name)
    else:
        raise Exception('Not string')


def test_name_records_not_empty(name):
    if len(name) > 0:
        make_name_record(name)
    else:
        raise Exception('Name is empty')

test_name_records()
test_name_records_by_string("Name")
test_name_records_not_empty("Name")