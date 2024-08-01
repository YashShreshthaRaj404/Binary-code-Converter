def binary_to_text(binary_input):
    binary_values = binary_input.split()
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    return ''.join(ascii_characters)


binary_code = input("Write a binary codes:")
text_output = binary_to_text(binary_code)
print(text_output) 

