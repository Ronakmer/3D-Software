from msilib.schema import File
from cryptography.fernet import Fernet

key = Fernet.generate_key()



# *********************** File Encrypt ***********************
f = Fernet(key)

with open('encrypted.json', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('files.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# *********************** File Dencrypt ***********************

f = Fernet(key)

with open('files.json', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_files.json', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)