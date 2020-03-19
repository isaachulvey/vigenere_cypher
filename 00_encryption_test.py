# vigenere cypher test

import pytest
from cf_vigenere_cypher import vigenere_scyther

def test_encryption():
	choice = "1"
	message = "this is a test message"
	key = "bingo"
	vs = vigenere_scyther(choice, message, key)
	print(choice, message, key)
	print("\nRunning 00_encryption_test...")
	assert vs.main() == "UPVYWTIGKGUURYGBOR"

def test_decryption():
	choice = "2"
	message = "UPVYWTIGKGUURYGBOR"
	key = "bingo"
	vs = vigenere_scyther(choice, message, key)
	print(choice, message, key)
	print("\nRunning 00_encryption_test...")
	assert vs.main() == "THISISATESTMESSAGE"