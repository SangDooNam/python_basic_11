"""Certainly! How about creating a Python program to encrypt and decrypt messages using a simple Caesar cipher? 
The Caesar cipher is a substitution cipher that shifts each letter in the plaintext by a certain number of positions down the alphabet. 
For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', etc.

Here are some specific tasks you could consider:

    Write a function encrypt(text, shift) that takes a string and an integer shift value, and returns the encrypted text.
    Write a function decrypt(encrypted_text, shift) that takes a string of encrypted text and an integer shift value, and returns the decrypted text.
    Create a main program loop where the user can choose to encrypt or decrypt a message, enter the message, and then see the result.
    Add error handling to deal with invalid inputs (like non-numeric shift values or other unexpected input).

This will give you practice with loops, string manipulation, and some basic encryption techniques."""




# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if character is upper-case or lower-case
            is_upper = char.isupper()

            # Convert character to its ASCII value
            char = char.lower()
            ascii_val = ord(char)

            # Perform the shift operation
            ascii_val = (ascii_val - ord('a') + shift) % 26 + ord('a')

            # Convert the new ASCII value back to a character
            new_char = chr(ascii_val)

            # Convert back to upper-case if necessary
            if is_upper:
                new_char = new_char.upper()

            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text


# Function to decrypt the text
def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


# Main program loop
while True:
    action = input("Do you want to encrypt or decrypt? (e/d/quit): ")
    if action == 'quit':
        break

    if action not in ['e', 'd']:
        print("Invalid choice, please try again.")
        continue

    text = input("Enter the text: ")
    shift = input("Enter the shift value: ")

    # Validate that shift value is an integer
    try:
        shift = int(shift)
    except ValueError:
        print("Invalid shift value, please enter an integer.")
        continue

    # Perform encryption or decryption based on the user's choice
    if action == 'e':
        result = encrypt(text, shift)
        print(f"Encrypted text: {result}")
    elif action == 'd':
        result = decrypt(text, shift)
        print(f"Decrypted text: {result}")



