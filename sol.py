class Err(Exception):
    pass

def process_list(s):
    input_list = [float(x) for x in s.split()]

    if not all(isinstance(item, int) or item.is_integer() for item in input_list):
        raise ValueError("Error: Please enter valid integers.")

    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise Err("Error: The list length must be a multiple of 10.")
    
    # Remove items at positions which are a multiple of 2 or 3
    processed_list = [int(item) for index, item in enumerate(input_list) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]

    # Print or return the processed list
    print("Processed List:", processed_list)
    return processed_list


# Example usage:
try:
    s = input("Enter a list of numbers separated by spaces: ")
    

    process_list(s)

except ValueError as ve:
    print(ve)
except Err as ile:
    print(ile)
