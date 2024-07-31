def text_to_binary(text):
    binary_result = []
    for char in text:
        # Get the ASCII value of the character and convert it to binary
        binary_char = format(ord(char), '08b')
        binary_result.append(binary_char)
    return ' '.join(binary_result)

word = input("Enter a number or a words / sentence " )
binary_code = text_to_binary(word)
print(f"The word '{word}' in binary is: {binary_code}")
