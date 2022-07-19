from cryptography.fernet import Fernet
import shutil
import os
from getmac import get_mac_address as gma

# *********************** get mac ***********************

# mac=gma()
# print("Your mac address=",mac)

# ***********************   ***********************

folderName = 'App'
fileName = folderName+'.zip'

# *********************** zip & delete folder ***********************

shutil.make_archive(folderName, 'zip', folderName)
shutil.rmtree(folderName)

# *********************** key make ***********************

# key = Fernet.generate_key()
key="DoWI-Hx4wP0QmO3Ze7kQhJXN7yeq2YFUOTr0G7iRKco=e8:2a:44:27:52:fa"
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

# # *********************** unzip & remove ***********************

shutil.unpack_archive(fileName, folderName)
os.remove(fileName)