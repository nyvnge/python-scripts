from cryptography.fernet import Fernet

def encrypt(text, key):
    fnt = Fernet(key)
    encrypted_text = fnt.encrypt(text.encode())
    return encrypted_text

def decrypt(encrypted_text, key):
    fnt = Fernet(key)
    decrypted_text = fnt.decrypt(encrypted_text).decode()
    return decrypted_text

text = input("Enter Text to process: ")
key = Fernet.generate_key()
encrypted_text = encrypt(text, key)
print("Encrypted Text: ", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Text: ", decrypted_text)

