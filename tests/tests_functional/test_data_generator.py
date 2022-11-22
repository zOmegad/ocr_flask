from data_generator import *

def test_generating_data():
    data_test = Data_generator()
    data_test.generate_data()
    assert data_test.result is True
