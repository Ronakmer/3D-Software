import zipfile
from cryptography.fernet import Fernet

# *********************** zip ***********************
# zip_files=zipfile.ZipFile('3d-software-gui--main.zip','w')
# zip_files.write('3d-software-gui--main',compress_type=zipfile.ZIP_DEFLATED)
# # zip_files.write('admin',compress_type=zipfile.ZIP_DEFLATED)
# zip_files.close()

# *********************** Encrypt key ***********************

key = Fernet.generate_key()
print(key)

# *********************** File Encrypt ***********************

# f = Fernet(key)

# with open('3d-software-gui--main.zip', 'rb') as original_file:
#     original = original_file.read()
    

# encrypted = f.encrypt(original)

# with open ('files.zip', 'wb') as encrypted_file:
#     encrypted_file.write(encrypted)


# *********************** File Dencrypt ***********************

f = Fernet(key)

with open('files.zip', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_file.zip', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)







# ********************* un zip *********************

# unzip_files=zipfile.ZipFile('dec_filess.zip','r')
# unzip_files.extractall('hi.zip')

