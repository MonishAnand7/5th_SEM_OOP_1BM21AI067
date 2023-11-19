def Encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

user_text = input("Enter the text to encrypt: ")
user_shift = int(input("Enter the shift value: "))

encrypted_result = Encrypt(user_text, user_shift)
print(f"The encrypted text is: {encrypted_result}")
