import sys 
from Crypto import Random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class Cryptor(object):

    def __init__(self):
        self.key = "a key for crypt!" 
        self.iv = Random.new().read(AES.block_size)
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        length=16
        count = len(text)
        if (count %length !=0):
            add = length - (count %length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)


    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text
