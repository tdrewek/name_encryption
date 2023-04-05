import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")


#ENCRYPT
print("\n")
plain_text = input("(*)Enter name/phrase to encrypt: ")
print("\n")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

#print(f"Before encryption : {plain_text}")
print(f"----> After  encryption : {cipher_text}")
print("\n")

#DECRYPT
cipher_text = input("(*) Enter encrypted message to decrypt: ")
print("\n")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

#print(f"Encrypted message : {cipher_text}")
print(f"----> Original  message : {plain_text}")
print("\n")