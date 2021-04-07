import json
import os
import random
from cryptography.fernet import Fernet

fpath = __file__
absolute_path = os.path.abspath(fpath)
base_dir = os.path.dirname(absolute_path)
epicPath = base_dir + '/passwords/'

def write_key():
    keyPath = base_dir + '/special/'
    file_name = keyPath + 'spec.key'

    key = Fernet.generate_key()
    if not os.path.exists(keyPath):
        os.mkdir(keyPath)
    with open(file_name, "wb") as key_file:
        key_file.write(key)

keyPath = base_dir + '/special/'
keyname = keyPath + 'spec.key'
if not os.path.exists(keyname):
    write_key()
    print("="*30, "Key Generator", "="*30)
    print("I have generated your SPECIAL key needed to DECRYPT your keys. Do NOT delete this, or your passwords will be lost!")
    print("="*75)
def name():
    tname = input("Enter name of password: ")
    if os.path.exists(epicPath + tname + '.txt'):
        print("Name is taken!")
        name()
    else:
        cont(tname)

def cont(name):
    email = input("Enter username/email: ")
    passphrase = input("Enter password: ")

    x = {"name": name, "email": email, "passphrase": passphrase}

    y = json.dumps(x)
    generate(y, name)

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        file.close()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
        file.close()

def load_key():
    fpath = __file__
    absolute_path = os.path.abspath(fpath)
    base_dir = os.path.dirname(absolute_path)
    epicPath = base_dir + '/special/'
    file_name = epicPath + 'spec.key'
    return open(file_name, "rb").read()

def save(load, full_path):
    folder = base_dir + '/passwords/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(full_path, "w") as key_file:
        key_file.write(load)
        key_file.close()
    key = load_key()
    encrypt(full_path, key)

def generate(y, name):
    full_path = epicPath + name + '.txt'
    save(y, full_path)

name()

