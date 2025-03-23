def ascii_converter(text):
    print('This ASCII converter supports all characters and codes from 0 to 255.')
    print('Enter a character or ASCII code to convert it to ASCII code or character.')
    print('Type "exit" to quit\n.')
    
    # Dictionary for common control character names
    control_chars = {
        0: 'Null (NUL)', 1: 'Start of Heading (SOH)', 2: 'Start of Text (STX)',
        3: 'End of Text (ETX)', 4: 'End of Transmission (EOT)', 5: 'Enquiry (ENQ)',
        6: 'Acknowledge (ACK)', 7: 'Bell (BEL)', 8: 'Backspace (BS)', 9: 'Horizontal Tab (HT)',
        10: 'Line Feed (LF)', 11: 'Vertical Tab (VT)', 12: 'Form Feed (FF)', 13: 'Carriage Return (CR)',
        14: 'Shift Out (SO)', 15: 'Shift In (SI)', 16: 'Data Link Escape (DLE)', 17: 'Device Control 1 (DC1)',
        18: 'Device Control 2 (DC2)', 19: 'Device Control 3 (DC3)', 20: 'Device Control 4 (DC4)',
        21: 'Negative Acknowledge (NAK)', 22: 'Synchronous Idle (SYN)', 23: 'End of Transmission Block (ETB)',
        24: 'Cancel (CAN)', 25: 'End of Medium (EM)', 26: 'Substitute (SUB)', 27: 'Escape (ESC)',
        28: 'File Separator (FS)', 29: 'Group Separator (GS)', 30: 'Record Separator (RS)',
        31: 'Unit Separator (US)', 127: 'Delete (DEL)'
    }
    
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
                    if ascii_code in control_chars:
                        print(f'The ASCII code {ascii_code} is {control_chars[ascii_code]}')
                    else:
                        print(f'The character of ASCII code {ascii_code} is "{char}".')
                else:
                    print(f'Error: {ascii_code} is not an ASCII code.')
            except ValueError:
                print('Error: Invalid input.')
                
                
                
if __name__ == '__main__':
    ascii_converter('text')