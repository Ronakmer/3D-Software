
from cryptography.fernet import Fernet



key = Fernet.generate_key()
print(key)

# string="ub0e86S6Sai4MXlAO3uVVmsp3JZAea1ZkktBv5bnOqo="
# print(len(string))

# *********************** File Encrypt ***********************

f = Fernet(key)

with open('hi.txt', 'rb') as original_file:
    original = original_file.read()
    

encrypted = f.encrypt(original)

with open ('files.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# *********************** File Dencrypt ***********************

f = Fernet(key)

with open('files.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_files.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)




# orig_key = b64decode(b'Rm5EPJai72qcK3RGBpW3vPNfZy5OZothY+kHY6h21KM=')
# enc_key = blake2s(key=orig_key, person=b'kEncrypt').digest()
# mac_key = blake2s(key=orig_key, person=b'kMAC').digest()
# print(b64encode(enc_key).decode('utf-8'))

# print(b64encode(mac_key).decode('utf-8'))

