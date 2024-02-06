# List Processing Python Program

This Python program takes a list of integers as input, performs specific operations on the list based on certain conditions, and provides error handling. The program includes a custom exception for handling invalid list lengths.
Solution Overview

The solution is implemented in the process_list.py file. The key features include:

    Accepts a list of integers as input.
    Verifies whether the length of the input list is a multiple of 10; otherwise, it raises a custom InvalidListLengthError with an appropriate error message.
    Removes items at positions that are multiples of 2 or 3 from the input list.
    Prints or returns the processed list.

# Error Handling

The program includes error handling to ensure the input meets the specified requirements:

    If the list length is not a multiple of 10, it raises an InvalidListLengthError with an informative error message.
    If the input contains non-integer elements, a ValueError is raised.
# Unit Tests

Unit tests are provided in the test_process_list.py file using the unittest framework. The tests cover various scenarios:

    test_valid_list_length: Tests whether the function works correctly for a valid input list length.
    test_invalid_list_length: Tests whether the function raises the expected InvalidListLengthError for an invalid input list length.
    test_invalid_input: Tests whether the function raises a ValueError for invalid input.
    test_float_input: Additional test for decimal inputs. For Example the input [1,2.0,3,4,5,6,7,8,9,10] it should pass but for the input [1,2.5,3,4,5,6,7,8,9,10] it should fail as 2.5 is not an integer

To run the tests, execute the test_process_list.py file. A successful run will indicate that all tests passed, while any failures will provide information about the specific test(s) that failed.

Feel free to modify the program, add more tests, or adapt it to suit your specific requirements.
