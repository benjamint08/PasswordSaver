import tkinter
import os
import sys
from cryptography.fernet import Fernet
import json

fpath = __file__
absolute_path = os.path.abspath(fpath)
base_dir = os.path.dirname(absolute_path)
epicPath = base_dir + '/passwords/'

def Pass():
    folder = base_dir + '/passwords/'
    full_path = folder + name_msg.get() + '.txt'
    x = {"name": name_msg.get(), "email": email_msg.get(), "passphrase": pass_msg.get()}
    load = json.dumps(x)
    if not os.path.exists(folder):
        os.mkdir(folder)
    if not os.path.exists(full_path):
        with open(full_path, "w") as key_file:
            key_file.write(load)
            key_file.close()
            key = load_key()
            name_msg.set("")
            email_msg.set("")
            pass_msg.set("")
            encrypt(full_path, key)
    else:
        name_msg.set("Name is taken!")

def load_key():
    fpath = __file__
    absolute_path = os.path.abspath(fpath)
    base_dir = os.path.dirname(absolute_path)
    epicPath = base_dir + '/special/'
    file_name = epicPath + 'spec.key'
    return open(file_name, "rb").read()

def write_key():
    keyPath = base_dir + '/special/'
    file_name = keyPath + 'spec.key'

    key = Fernet.generate_key()
    if not os.path.exists(keyPath):
        os.mkdir(keyPath)
    with open(file_name, "wb") as key_file:
        key_file.write(key)

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

top = tkinter.Tk()
top.title("Save Password GUI")

messages_frame = tkinter.Frame(top)
name_msg = tkinter.StringVar()  # For the messages to be sent.
name_msg.set("Name here")
email_msg = tkinter.StringVar()  # For the messages to be sent.
email_msg.set("Email here")
pass_msg = tkinter.StringVar()  # For the messages to be sent.
pass_msg.set("Password here")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
entry_field_msg = tkinter.Entry(top, textvariable=name_msg)
entry_field_msg.pack()
entry_field_email = tkinter.Entry(top, textvariable=email_msg)
entry_field_email.pack()
entry_field_pass = tkinter.Entry(top, textvariable=pass_msg)
entry_field_pass.pack()
send_button = tkinter.Button(top, text="Save", command=Pass)
send_button.pack()

keyPath = base_dir + '/special/'
keyname = keyPath + 'spec.key'
if not os.path.exists(keyname):
    write_key()
tkinter.mainloop()