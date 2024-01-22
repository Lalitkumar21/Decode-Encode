from cryptography.fernet import Fernet
import os

def decode():
    files=[]
    for file in os.listdir():
        if file=="encoding.py" or file =="thekey.key" or file=="decoding.py" or file=="main.py":
            continue
        if os.path.isfile(file):
            files.append(file)
    print("Files to be decrypted:",files)

    with open("thekey.key",'rb') as key:
        secret_key=key.read()
        
    f=Fernet(secret_key)

    for file in files:
        with open(file,'rb') as thefile:
            contents=thefile.read()
        contents_decrypted = f.decrypt(contents)
        with open(file,'wb') as thefile:
            thefile.write(contents_decrypted)
            print("Files decrypted")


