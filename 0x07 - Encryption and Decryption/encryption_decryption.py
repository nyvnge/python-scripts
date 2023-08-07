from cryptography.fernet import Fernet

#Function to encrypt plain text using Fernet encryption
def encrypt(text, key):
    fnt = Fernet(key)
    encrypted_text = fnt.encrypt(text.encode())
    return encrypted_text

#Function to decrypt encrypted text using Fernet decryption
def decrypt(encrypted_text, key):
    fnt = Fernet(key)
    decrypted_text = fnt.decrypt(encrypted_text).decode()
    return decrypted_text

#User Input
text = input("Enter Text to process: ")

#Generates random secret Key
key = Fernet.generate_key()

#Outputs the secret key
print("Secret Key:", key.decode())

#Encrypt user input using the encypt function
encrypted_text = encrypt(text, key)

#Outputs encrypted text
print("Encrypted Text: ", encrypted_text)

#Decrypt encrypted text using decrypt function
decrypted_text = decrypt(encrypted_text, key)

#Outputs decrypted text
print("Decrypted Text: ", decrypted_text)



