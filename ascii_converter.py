def ascii_converter(text):
    print('This ASCII converter supports all characters and codes from 0 to 255.')
    print('Enter a character or ASCII code to convert it to ASCII code or character.')
    print('Type "exit" to quit\n.')
    while True:
        user_input = input('Enter a character or ASCII code: ').strip()
        if user_input.lower() == 'exit':
            break
        
    # Character to ASCII code
        if len(user_input) == 1:
            char = user_input
            ascii_code = ord(char)
            if ascii_code <= 255:
                print(f'The ASCII code of "{char}" is {ascii_code}. (Hex: {hex(ascii_code)})')
            else:
                print(f'Error: "{char}" is not an ASCII character.')
                
    # ASCII code to character
        else:
            try:
                ascii_code = int(user_input)
                if 0 <= ascii_code <= 255:
                    char = chr(ascii_code)
                    print(f'The character of ASCII code {ascii_code} is "{char}".')
                else:
                    print(f'Error: {ascii_code} is not an ASCII code.')
            except ValueError:
                print('Error: Invalid input.')
                
                
                
if __name__ == '__main__':
    ascii_converter('text')