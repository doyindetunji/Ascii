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
        31: 'Unit Separator (US)', 127: 'Delete (DEL)',
         # Extended ASCII controls (128-159)
        128: 'Padding Character (PAD)', 129: 'High Octet Preset (HOP)', 130: 'Break Permitted Here (BPH)',
        131: 'No Break Here (NBH)', 132: 'Index (IND)', 133: 'Next Line (NEL)', 134: 'Start of Selected Area (SSA)',
        135: 'End of Selected Area (ESA)', 136: 'Horizontal Tab Set (HTS)', 137: 'Horizontal Tab Justify (HTJ)',
        138: 'Vertical Tab Set (VTS)', 139: 'Partial Line Down (PLD)', 140: 'Partial Line Up (PLU)',
        141: 'Reverse Line Feed (RI)', 142: 'Single-Shift 2 (SS2)', 143: 'Single-Shift 3 (SS3)',
        144: 'Device Control String (DCS)', 145: 'Private Use 1 (PU1)', 146: 'Private Use 2 (PU2)',
        147: 'Set Transmit State (STS)', 148: 'Cancel Character (CCH)', 149: 'Message Waiting (MW)',
        150: 'Start of Protected Area (SPA)', 151: 'End of Protected Area (EPA)', 152: 'Start of String (SOS)',
        153: 'Single Graphic Char Intro (SGCI)', 154: 'Single Character Intro (SCI)', 155: 'Control Sequence Intro (CSI)',
        156: 'String Terminator (ST)', 157: 'Operating System Command (OSC)', 158: 'Privacy Message (PM)',
        159: 'Application Program Command (APC)'
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