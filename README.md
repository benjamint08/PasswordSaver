# passwordsaver
a nice and easy way to save your passwords, entirely made out of python, with a secure encryption.
<br>

# what is it?

PasswordSaver is a semi-secure password saver with encryption created in Python 3.9.

# reviews

<img width="295" alt="Screenshot 2021-04-07 at 12 40 20" src="https://user-images.githubusercontent.com/61296321/113860879-721c0d00-979e-11eb-808d-8af4c38f6fee.png">

# how do I use it?

First, if you don't have it, install '[pip](https://github.com/pypa/pip/releases/tag/21.0.1)' (installation guide [here](#installing-pip)) , it's required for this as it installs the required Python libraries.

Then, go in to your terminal and CD to this folder, then you need to type:

`python3.9 -m pip install cryptography`

And it should install the required library 'Cryptography'.

Next you want to run `save-password.py` using `Python 3.9`.

It should ask for a Name of the password, then Email/Username, then password.

It then encrypts the JSON and saves it to /password/(name).txt

Then to get the password, open `get-password.py` in `Python 3.9` and enter the name of the password you saved. It displays it in your Terminal, and keeps it encrypted.
It should look like this:

` "name": "Password Name", "email": "text@example.com", "passphrase": "test"}`

"email" is your Username/Email, "passphrase" is your Password.

# editing password

Just open `edit-password.py` in `Python 3.9` and type the name in, then enter your new username and password and it edits and encrypts!

# deleting password

Open `delete-password.py` in `Python 3.9` and type the file name in. It will display its decrypted contents just in case.

# any help/questions?

<br>
Message me on Discord: `emma!!#0088`

# installing pip

Download [pip](https://github.com/pypa/pip/releases/tag/21.0.1), then unzip it, go in to your terminal and CD to the folder, and type:
`python3.9 setup.py install`. It should install pip.
