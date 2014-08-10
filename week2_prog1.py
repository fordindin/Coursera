#!/usr/bin/env python

import pycryptopp.cipher.aes as aes
import Crypto.Cipher.AES as AES
from cryptolib import *
import sys

cbc_key = '140b41b22a29beb4061bda66b6747e14'
cbc_ct = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
cbc_ct = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

ctr_key = '36f18357be4dbd77f050515c73fcf9f2'
ctr_ct = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'

def decrypt_once(msg, key=cbc_key):
		cryptor = AES.new(key)
		return data2hex(cryptor.encrypt(msg))

def cbc_decrypt(key, ct):
		block_ct = msg2bs(ct, blocksize=16)
		iv = block_ct.pop(0)
		round_xor = iv
		out = []
		for b in block_ct:
				dblock = decrypt_once(hex2data(b), key=key)
				oblock = "".join(sxor(dblock, round_xor))
				round_xor = b
				out.append(hex2data(oblock))
		out = "".join(out)
		last_byte = int(ord(out[-1]))
		out = out[:-last_byte]
		return out

def ctr_decrypt(key, ct):
		block_ct = msg2bs(ct, blocksize=16)
		iv = block_ct.pop(0)
		out = []
		for i in range(len(block_ct)):
				round_xor = decrypt_once(hex(int(iv, 16)+i)[2:-1], key=ctr_key)
				out.append("".join(sxor(block_ct[i], round_xor)))
		return hex2data("".join(out))




		#print iv, hex(iv_int)[2:-1]
		#ct = cryptor.process(m)

#print cbc_decrypt(cbc_key, cbc_ct)
print ctr_decrypt(ctr_key, ctr_ct)
