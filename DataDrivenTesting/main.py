
from fuzzywuzzy import fuzz
from DataDrivenTesting.utile import validation, get_input_data, test_driven


def test_case(input_data, expected_data):
    similarity = fuzz.partial_ratio(input_data, expected_data)
    validation(similarity)
    return similarity


if __name__ == '__main__':
    data = get_input_data("D:/Testing Recordings/PythonTesting-main/DataDrivenTesting/TestData/input_data.json")
    print(data)
    print()
    output = test_driven(data, test_case)
    print(output)





