import tkinter
import os
import sys
from cryptography.fernet import Fernet
import json
import random

fpath = __file__
absolute_path = os.path.abspath(fpath)
base_dir = os.path.dirname(absolute_path)
epicPath = base_dir + '/passwords/'

keyPath = base_dir + '/special/'
passlockname = keyPath + 'lock.pws'

def Pass():
    folder = base_dir + '/passwords/'
    full_path = folder + name_msg.get() + '.pwsaver'
    if not os.path.exists(full_path):
        name_msg.set("File doesnt exist")
    else:
        key = load_key()
        decrypt(full_path, key)

def Clear():
    email_text.set("")
    pass_text.set("")
    pass_lock_msg.set("")
    name_msg.set("")

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

def decrypt(filename, key):
    f = Fernet(key)
    if not os.path.exists(passlockname):
        print("Use save-password.py to generate your decryption key :(")
        sys.exit()
    with open(passlockname, "rb") as file:
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
        file.close()
    os.remove(decfile)
    os.rmdir(decdir)
    if not pass_lock_msg.get() == e:
        sys.exit()
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
        k = json.loads(e)
        email_text.set(k['email'])
        pass_text.set(k['passphrase'])
        pass_lock_msg.set("")
        file.close()
    os.remove(decfile)
    os.rmdir(decdir)

top = tkinter.Tk()
top.title("Get Password GUI")

if not os.path.exists(passlockname):
    messages_frame = tkinter.Frame(top)
    name_msg = tkinter.StringVar()  # For the messages to be sent.
    name_msg.set("Run save-password.py")
    name_msg_2 = tkinter.StringVar()
    name_msg_2.set("for decryption key!")
    entry_field_msg = tkinter.Entry(top, textvariable=name_msg)
    entry_field_msg.pack()
    entry_field_msg_2 = tkinter.Entry(top, textvariable=name_msg_2)
    entry_field_msg_2.pack()
else:
    messages_frame = tkinter.Frame(top)
    name_msg = tkinter.StringVar()  # For the messages to be sent.
    name_msg.set("Name here")
    pass_lock_msg = tkinter.StringVar()
    pass_lock_msg.set("Pass lock here")
    pass_lock = tkinter.Entry(top, textvariable=pass_lock_msg)
    pass_lock.pack()
    scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
    entry_field_msg = tkinter.Entry(top, textvariable=name_msg)
    entry_field_msg.pack()
    send_button = tkinter.Button(top, text="Get", command=Pass)
    send_button.pack()
    clear_btn = tkinter.Button(top, text="Clear", command=Clear)
    clear_btn.pack()
    email_text = tkinter.StringVar()
    pass_text = tkinter.StringVar()
    a = tkinter.Entry(top, textvariable=email_text)
    a.configure(state='readonly')
    a.pack()
    b = tkinter.Entry(top, textvariable=pass_text)
    b.configure(state='readonly')
    b.pack()

keyname = keyPath + 'spec.key'
if not os.path.exists(keyname):
    write_key()
tkinter.mainloop()
