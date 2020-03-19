# vigenere cypher

from string import ascii_uppercase
from itertools import cycle
import string

# C = (M + K) mod 26
# M = (C - K) mod 26

class vigenere_scyther:
    def __init__(self, choice, message, key):
      # create base alphabet
      self.keys = [k for k in range(0,26)]
      self.values = list(ascii_uppercase)
      self.alphabet = dict(zip(self.keys, self.values))

      # get user inputs
      self.choice = choice
      self.message = self.__cleanup(message)
      self.key = self.__cleanup(key)

    # retrieve numeric value from alphabet dict
    def __get_key(self, val):
      for key, value in self.alphabet.items():
        if val == value:
          return key
      return "Key does not exist."
        
    # remove spaces and punctuation from input
    def __cleanup(self, text):
      clean = text.replace(" ", "").upper().translate(str.maketrans('', '', string.punctuation))
      return ''.join([i for i in clean if not i.isdigit()])

    # take message letter and key letter, return encoded letter
    def __encode(self, pair):
      return (self.__get_key(pair[0]) + self.__get_key(pair[1])) % 26

    # take message letter and key letter, return decoded letter
    def __decode(self, pair):
      return (self.__get_key(pair[0]) - self.__get_key(pair[1])) % 26

    # take input message, generate [msg, key] list, encode each letter, return numerical values
    def __encryption(self):
      input_list = [l for l in self.message]
      pairs = [[m, k] for m, k in zip(self.message, cycle(self.key))]
      for pair in pairs:
        encoded_message = [self.__encode(pair) for pair in pairs]
      return encoded_message

    # transform encoded message from numbers to letters
    def __transformation(self, method):
      return ''.join([self.alphabet.get(k) for k in method])
       
    # take input message, generate [msg, key] list, decode each letter, return numerical values
    def __decryption(self):
      input_list = [l for l in self.message]
      pairs = [[m, k] for m, k in zip(self.message, cycle(self.key))]
      for pair in pairs:
        decoded_message = [self.__decode(pair) for pair in pairs]
      return decoded_message

    # main, let's ride!
    def main(self):
      if self.choice == "1":
        output = self.__transformation(self.__encryption())
        print(f'Encrypted message: {output}')
      elif self.choice == "2":
        output = self.__transformation(self.__decryption())
        print(f'Decrypted message: {output}')
      return output

if __name__ == "__main__":
  print("Welcome to Isaac's Vigenere Cypher!")
  choice = input("Enter 1 to encrypt a message or 2 to decrypt a message: " )
  
  if choice not in ["1","2"]:
    raise Exception("I asked you to enter 1 or 2, and you couldn't even do that")
  
  message = input("Enter your message: ")
  key = input("Enter your key: ")

  vs = vigenere_scyther(choice, message, key)
  vs.main()
