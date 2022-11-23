from data_generator import DataGenerator

def test_generating_data():
    data_test = DataGenerator()
    data_test.generate_data()
    assert data_test.result is True
