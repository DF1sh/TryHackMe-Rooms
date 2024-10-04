import string 

def decrypt(hex_encoded, key):
    # Step 1: Hex-decode the encrypted string back to bytes
    xorred_bytes = bytes.fromhex(hex_encoded)
    
    # Step 2: Perform XOR between xorred_bytes and the key to get the original flag
    decrypted_flag = ''
    for i in range(len(xorred_bytes)):
        decrypted_flag += chr(xorred_bytes[i] ^ ord(key[i % len(key)]))
    
    return decrypted_flag

def setup(flag, key):
    # XOR operation with the given flag and key
    xored = ""
    for i in range(0, len(flag)):
        xored += chr(ord(flag[i]) ^ ord(key[i % len(key)]))
    
    # Hex encode the result of the XOR operation
    hex_encoded = xored.encode().hex()
    return hex_encoded

def brute_force_key(keyNoHex, hexAndXorredFlag1):
    flag = 'THM{thisisafakeflag}'  # The same flag used in encryption
    # Step 1: Take the first 4 characters of the key
    base_key = keyNoHex[:4]

    # Step 2: Iterate through ASCII letters and digits only (string.ascii_letters + string.digits)
    possible_characters = string.ascii_letters + string.digits
    for char in possible_characters:
        # Step 3: Create the KeyNoHexTest by appending the character to base_key
        keyNoHexTest = base_key + char
        
        # Step 4: Perform encryption with the keyNoHexTest
        #hex_encoded = setup(flag, keyNoHexTest)

        dec = decrypt(hexAndXorredFlag1, keyNoHexTest)

        
        # Print the key being tested and the resulting hex-encoded XOR
        print(f"KeyNoHexTest: {keyNoHexTest} -> Decrypted result (hex): {dec}")

def first(hexAndXorredFlag1):
    key_length = 5
    plainFlag1NoHex = 'THM{'  # Plain string (not hex-encoded)

    # Step 1: Decode the hex-encoded XORed flag into bytes (returns bytes)
    xorredFlag1 = bytes.fromhex(hexAndXorredFlag1)

    unhexed_xorredFlag1 = ''.join(chr(b) for b in xorredFlag1)

    # Print the unhexadecimaled xorredFlag1
    print("UNHEX:", xorredFlag1)


    
    # Step 2: Perform XOR between xorredFlag1 and plainFlag1NoHex, save in keyNoHex
    keyNoHex = ''
    for i in range(len(plainFlag1NoHex)):
        # Get the integer (ASCII) value of the plain character
        plain_char = plainFlag1NoHex[i]
        plain_ord = ord(plain_char)  # ASCII value of the plain character

        # XOR the decoded byte (from xorredFlag1) with the plain flag's ASCII value
        xorred_byte = xorredFlag1[i]  # This is an integer (byte value)
        xor_result = xorred_byte ^ plain_ord  # Perform XOR between the byte and ASCII value

        # Convert XOR result back to a character and add to keyNoHex
        keyNoHex += chr(xor_result)

        # Print values at each step for debugging
        # print(f"Step {i + 1}:")
        #print(f"  Plain character: '{plain_char}' (ord: {plain_ord})")
        #print(f"  XORed value from hex: {xorred_byte} (byte)")
        #print(f"  XOR result: '{chr(xor_result)}'")

    # Step 3: Convert keyNoHex to hexadecimal
    keyHex = keyNoHex.encode().hex()

    # Print the resulting key in both plain and hex format
    print("\nkeyNoHex (XOR result, plain):", keyNoHex)
    print("keyHex (XOR result, hex):", keyHex)

    # Print the first 5 characters of keyNoHex and keyHex
    print("\nFirst 4 characters of keyNoHex (plain):", keyNoHex[:4])
    print("First 4 characters of keyHex (hex):", keyHex[:8])
    return keyNoHex

if __name__ == '__main__':
    # Example input: the hex-encoded XORed flag
    hexAndXorredFlag1 = input("Please enter the hex-encoded XORed flag: ")
    k=first(hexAndXorredFlag1)
    brute_force_key(k, hexAndXorredFlag1)
