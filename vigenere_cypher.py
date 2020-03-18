# vigenere cypher

from string import ascii_uppercase
from itertools import cycle
import string

# C = (M + K) mod 26
# M = (C - K) mod 26

# create base alphabet
keys = [k for k in range(0,26)]
values = list(ascii_uppercase)
alphabet = dict(zip(keys, values))

# retrieve numeric value from alphabet dict
def get_key(val):
	for key, value in alphabet.items():
		if val == value:
			return key
	return "Key does not exist."

# remove spaces and punctuation from input
def cleanup(text):
	clean = text.replace(" ", "")
	clean = clean.upper()
	clean = clean.translate(str.maketrans('', '', string.punctuation))
	clean = ''.join([i for i in clean if not i.isdigit()])
	return clean

# take message letter and key letter, return encoded letter
def encode(pair):
	encoded_letter = (get_key(pair[0]) + get_key(pair[1])) % 26
	return encoded_letter

# take message letter and key letter, return decoded letter
def decode(pair):
	decoded_letter = (get_key(pair[0]) - get_key(pair[1])) % 26
	return decoded_letter

# take input message, generate [msg, key] list, encode each letter, return numerical values
def encryption(msg, key):
	input_list = [l for l in msg]
	pairs = [[m, k] for m, k in zip(msg, cycle(key))]
	for pair in pairs:
		encoded_message = [encode(pair) for pair in pairs]
	return encoded_message

# transform encoded message from numbers to letters
def transformation(encoded_message):
	output = [alphabet.get(key) for key in encoded_message]
	return ''.join(output)

# take input message, generate [msg, key] list, decode each letter, return numerical values
def decryption(msg, key):
	input_list = [l for l in msg]
	pairs = [[m, k] for m, k in zip(msg, cycle(key))]
	for pair in pairs:
		decoded_message = [decode(pair) for pair in pairs]
	return decoded_message

print("Welcome to Isaac's Vigenere Cypher!")
choice = input("Enter 1 to encrypt a message or 2 to decrypt a message." )

if choice == "1":
	message = input("Enter your message: ")
	message = cleanup(message)
	key = input("Enter your key: ")
	key = cleanup(key)
	output = transformation(encryption(message, key))
	print(f"Encrypted message: {output}")
elif choice == "2":
	message = input("Enter your message: ")
	message = cleanup(message)
	key = input("Enter your key: ")
	key = cleanup(key)
	output = transformation(decryption(message, key))
	print(f"Decrypted message: {output}")
else:
	print("Invalid choice. Please enter 1 or 2.")