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
            print(f'The ASCII code of "{char}" is {ascii_code}.')