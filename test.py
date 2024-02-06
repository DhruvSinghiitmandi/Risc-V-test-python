import unittest
from sol import process_list, Err

class TestProcessList(unittest.TestCase):
    def test_valid_list_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        processed_list = process_list(input_list)
        expected_result = [1, 4, 5, 7, 9, 11, 13, 16, 17, 19]
        self.assertEqual(processed_list, expected_result)

    def test_invalid_list_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(Err) as context:
            process_list(input_list)
        self.assertEqual(str(context.exception), "Error: The list length must be a multiple of 10.")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            input_list = [1, 2, 'invalid', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
            process_list(input_list)
    
    def test_float_input(self):
        with self.assertRaises(ValueError):
            input_list = [1, 2, 2.0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
            process_list(input_list)

if __name__ == '__main__':
    unittest.main()