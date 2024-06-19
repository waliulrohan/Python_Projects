import os

from cryptography.fernet import Fernet

files =[]

for file in os.listdir():
    if file == "encrypt.py" or  file == 'thekey.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):    
       files.append(file)

with open("thekey.key" , "rb") as key:
    secretkey = key.read()

secret_pass = "password"

user_input_pass = input("Enter secret pass to continue: ")

if secret_pass == user_input_pass:
    for file in files:
        with open(file , 'rb') as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file , "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats. All your files are decrypted.")            
else:
    print("Wrong secret pass. Try again.")