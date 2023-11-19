def Encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

def Decrypt(text, shift):
    return Encrypt(text, -shift)

user_text = input("Enter the text to encrypt: ")
shift_amount = int(input("Enter the shift amount for encryption: "))

encrypted_text = Encrypt(user_text, shift_amount)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = Decrypt(encrypted_text, shift_amount)
print(f"Decrypted text: {decrypted_text}")
