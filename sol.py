class Err(Exception):
    pass

def process_list(input_list):
    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise Err("Error: The list length must be a multiple of 10.")
    
    # Remove items at positions which are a multiple of 2 or 3
    processed_list = [item for index, item in enumerate(input_list) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]

    # Print or return the processed list
    print("Processed List:", processed_list)
    return processed_list

# Example usage:
try:
   input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
  #  process_list(input_list)
except ValueError:
    print("Error: Please enter valid integers.")
except Err as e:
    print(e)