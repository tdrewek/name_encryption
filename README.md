# name_encryption

A simple python program to encrypt a name or phrase. This algorithm will always encrypt the name/phrase in a different way each time the program is executed. A new key is generated at random upon run-time. Therefore, it will be impossible to decrypt the same name/phrase with the same key after the program has finished running. You should expext to see different encrypted results each time the program is executed.

## Disclaimer

As of right now, this program is only a demonstration of my knowledge on encryption for a class homework assignment. In the future, I plan to revisit this project increasing the complexity and usability. The random key generation upon run-time is not practical, but I have implemented it to show knowledge for the assignment. Later, I plan to remove this feature and implement a more sophisticated and reasonable key encryption algorithm. Thank you! 

## Installation/Download

Python will be required to be installed on your system to run this program. 
The latest version of Python is recommended but not required.

You may choose to clone the repository:

```bash
git clone https://github.com/tdrewek/name_encryption.git
```
Or you may choose to download the zip file [here](https://github.com/tdrewek/name_encryption/archive/refs/heads/main.zip).

## Usage

Open a terminal/console and navigate to the folder "name_encryption" if cloned or "name_encryption-main" if downloaded.

Once in the directory, you can run the program one of two ways depending on the Python version you have installed on your system:

If using Python v3.x.x run:
```bash
python3 main.py
```

If using Python v2.x.x or older, run:
```bash
python main.py
```

## Example

```bash
(*)Enter name/phrase to encrypt: This is my secret message: Dunkin is better than Starbucks!


----> After  encryption : 9@#(W#(WbYW(eo_ezWbe((j-e]W$U<G#<W#(WEezze_Wz@j<Whzj_EUoG(6


(*) Enter encrypted message to decrypt: 9@#(W#(WbYW(eo_ezWbe((j-e]W$U<G#<W#(WEezze_Wz@j<Whzj_EUoG(6


----> Original  message : This is my secret message: Dunkin is better than Starbucks!
```



