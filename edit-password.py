from cryptography.fernet import Fernet
import os
import random
import json
import argparse,sys

fpath = __file__
absolute_path = os.path.abspath(fpath)
base_dir = os.path.dirname(absolute_path)
epicPath = base_dir + '/passwords/'

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
        print("File edited and encrypted successfully.")

def decrypt(filename, key, name):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        file.close()
    decrypted_data = f.decrypt(encrypted_data)
    decdir = base_dir + '/decpass/'
    if not os.path.exists(decdir):
        os.mkdir(decdir)
    decfile = decdir + 'dec-' + str(random.randrange(0,500000)) + '.pwsaver'
    with open(decfile, "wb") as file:
        file.write(decrypted_data)
        file.close()
    with open(decfile, "r") as file:
        e = file.read()
        pp = json.loads(e)
        print("="*40, "Decrypted Password", "="*40)
        print("Name - ",pp['name'])
        print("User/Email - ",pp['email'])
        print("Password - ",pp['passphrase'])
        print("=" * 40, "Decrypted Password", "=" * 40)
        file.close()
    newuser = input("Enter new username: ")
    newpass = input("Enter new pass: ")
    j = {"name": name, "email": newuser, "passphrase": newpass}
    x = json.dumps(j)
    with open(filename, "w") as file:
        file.truncate()
        file.write(str(j))
        file.close()
    encrypt(filename, key)
    os.remove(decfile)
    os.rmdir(decdir)

def load_key():
    fpath = __file__
    absolute_path = os.path.abspath(fpath)
    base_dir = os.path.dirname(absolute_path)
    epicPath = base_dir + '/special/'
    file_name = epicPath + 'spec.key'
    return open(file_name, "rb").read()

def start():
    id = input("Enter name of password: ")
    full_path = epicPath + id + '.pwsaver'
    key = load_key()
    if os.path.exists(full_path):
        decrypt(full_path, key, id)
    else:
        print("File does not exist!")
        start()

parser = argparse.ArgumentParser()
parser.add_argument("-N", "--name", help="get a password")
parser.add_argument("-E", "--edit", help="edit", action="store_true")
args = parser.parse_args()

if args.edit:
    if args.name:
        full_path = epicPath + args.name + '.pwsaver'
        key = load_key()
        if os.path.exists(full_path):
            decrypt(full_path, key, args.name)
        else:
            print("File does not exist!")
            sys.exit()
    else:
        start()
else:
    start()
