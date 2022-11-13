from dz_9 import make_name_record

def test_name_records():
    name_1 = make_name_record("John")
    name_2 = make_name_record("Name")
    name_3 = make_name_record("123")
    name_4 = make_name_record("1234")

test_name_records()