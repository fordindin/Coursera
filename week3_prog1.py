#!/usr/bin/env python

from Crypto.Hash import SHA256
import sys

def sha(indata):
		s = SHA256.new()
		s.update(indata)
		return s.digest()

f = open(sys.argv[1])

data = f.read()
block_data = []
f.close()

block_count = len(data)/1024
pad_length = len(data)%1024

for b in range(block_count):
		block_data.append(data[b*1024: (b+1)*1024])

if pad_length != 0:
		block_data.append(data[block_count*1024:])

last_hashblock = ''
for b in range(len(block_data), 0, -1):
		last_hashblock = sha(block_data[b-1]+last_hashblock)

print last_hashblock.encode('hex')
