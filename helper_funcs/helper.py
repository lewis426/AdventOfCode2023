def list_of_chars(input:str)->list:
    '''Splits an AoC input into respective lines, and then splits 
    each line into a list of characters

    Args:
      input: str
        The AoC input as a string
    
    Returns:
      a list where each element is a line in the input
    '''
    input = input.splitlines()
    for idx, inp in enumerate(input):
        input[idx] = [char for char in inp]

    return input