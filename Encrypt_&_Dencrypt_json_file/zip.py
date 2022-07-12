from cryptography.fernet import Fernet
import shutil
import os

folderName = 'App'
fileName = folderName+'.zip'

# *********************** zip & delete folder ***********************

shutil.make_archive(folderName, 'zip', folderName)
shutil.rmtree(folderName)

# *********************** key make ***********************

key = Fernet.generate_key()
print(key)

f = Fernet(key)

# *********************** encrypte folder ***********************

with open(fileName, 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open (fileName, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# *********************** decrypted folder ***********************

# f = Fernet(input('Enter Key: '))
f = Fernet(key)
with open(fileName, 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open(fileName, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

# *********************** unzip & remove ***********************

shutil.unpack_archive(fileName, folderName)
os.remove(fileName)