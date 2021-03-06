# passwordsaver
a nice and easy way to save your passwords, entirely made out of python, with a seni-secure encryption and password lock.
<br>
<br>
<h1>== Important collapsibles! ==</h1>
<details>
  <summary>What is it?</summary>
PasswordSaver is a semi-secure password saver with encryption created in Python 3.9.
</details>

<br>

<details>
  <summary>Reviews</summary>
  <img width="295" alt="Screenshot 2021-04-07 at 12 40 20" src="https://user-images.githubusercontent.com/61296321/113860879-721c0d00-979e-11eb-808d-8af4c38f6fee.png">
</details>

<br>

<details>
<summary>Arguments (important!)</summary>
<h1>Saving a password with args</h1>
To save a password with args, CD to the folder and type:

`python3.9 save-password.py -S --name NAME --email EMAIL --password PASSWORD`
<br>
.. or type:
`python3.9 save-password.py --help`. All arguments are required for quick saving!
<br>
<h1>Editing a password with args</h1>
To save a password with args, CD to the folder and type:

`python3.9 edit-password.py -E --name NAME`
<br>
.. or type:
`python3.9 edit-password.py --help`. All arguments are required for quick editing!
<br>
<h1>Deleting a password with args</h1>
The same as the other two, CD to the folder and type:

`python3.9 delete-password.py --D --name NAME`
<br>
.. or type:
`python3.9 delete-password.py --help`. Again, all arguments are required for quick deleting!
</details>
<br>
<details>
<summary>Generating a random password</summary>
<br>
<details>
<summary>Inside the UI</summary>
<h1>inside the UI</h1>
To generate a random password inside the UI:

CD into the folder and type `python3.9 save-gui.py` and press Enter. Inside the UI press Generate. This will generate a random password for you.
</details>
<br>
<details>
<summary>Inside the CLI</summary>
<h1>in the CLI</h1>

CD into the folder and type `python3.9 save-password.py -S --name NAME --email EMAIL/USER --random LENGTH`

-S = Checking that you want to save<br>
--name NAME = Name of the file, example: --name GitHub<br>
--email EMAIL/USER = Username of website, example: --email test@example.com<br>
--random LENGTH = Generates a random password for you, example: --random 20 (generates a 20 character long password)
</details>
</details>
<br>
<details>
<summary>UI Saving/Getting</summary>
CD into the folder and type this to get the save UI:

`python3.9 save-gui.py`

You will know when your password saved when it clears the box contents.
To get your password, type:

`python3.9 get-gui.py`

..and enter the name of your password, the password lock and press Get. Simply press Clear when you have done looking at your password. Editing/Deleting will come soon.
</details>
<br>
<details>
<summary>UI Screenshots</summary>
<br>
Here are some screenshots of the new UI:
  <img width="226" alt="Screenshot 2021-04-07 at 16 26 31" src="https://user-images.githubusercontent.com/61296321/113892551-05186f80-97be-11eb-8ee6-864134cbfd5e.png">
  <img width="242" alt="Screenshot 2021-04-07 at 16 26 58" src="https://user-images.githubusercontent.com/61296321/113892613-15304f00-97be-11eb-92a8-e5f801cd38f4.png">
</details>

<h1>== Important collapsibles! ==</h1>

# how do I use it?

First, if you don't have it, install '[pip](https://github.com/pypa/pip/releases/tag/21.0.1)' (installation guide [here](#installing-pip)) , it's required for this as it installs the required Python libraries.

Then, go in to your terminal and CD to this folder, then you need to type:

`python3.9 -m pip install cryptography`

And it should install the required library 'Cryptography'.

Next you want to run `save-password.py` using `Python 3.9`.

It should ask for a password lock, this is an extra step needed to decrypt your passwords. Then the name of the password, then Email/Username, then password.

It then encrypts the JSON and saves it to /passwords/(name).txt

Then to get the password, open `get-password.py` in `Python 3.9` and enter the name of the password you saved. It displays it in your Terminal, and keeps it encrypted.
It should look like this:

`Name - GitHub (example)`
<br>`User/Email - test@example.com`<br>
`Password - password`

# editing password

Just open `edit-password.py` in `Python 3.9` and type the name in, then enter your new username and password and it edits and encrypts!

# deleting password

Open `delete-password.py` in `Python 3.9` and type the file name in. It will display its decrypted contents just in case.

# any help/questions?

<br>
Message me on Discord: 

`epic!!#0088`

# installing pip

Download [pip](https://github.com/pypa/pip/releases/tag/21.0.1), then unzip it, go in to your terminal and CD to the folder, and type:
`python3.9 setup.py install`. It should install pip.
