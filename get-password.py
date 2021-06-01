from cryptography.fernet import Fernet
import os
import random
import argparse,sys
import json

fpath = __file__
absolute_path = os.path.abspath(fpath)
base_dir = os.path.dirname(absolute_path)
epicPath = base_dir + '/passwords/'

def decrypt(filename, key):
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
        p = json.loads(e)
        print("Name - " + p['name'])
        print("User/Email - " + p['email'])
        print("Password - " + p['passphrase'])
        file.close()
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
        decrypt(full_path, key)
    else:
        print("File does not exist!")
        sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("-N", "--name", help="get a password")
parser.add_argument("-G", "--get", help="get", action="store_true")
args = parser.parse_args()

if args.get:
    if args.name:
        full_path = epicPath + args.name + '.pwsaver'
        key = load_key()
        if os.path.exists(full_path):
            decrypt(full_path, key)
        else:
            print("File does not exist!")
            sys.exit()
    else:
        start()
else:
    start()