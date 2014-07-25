#!/usr/bin/env python
import sys

def c2bs(m):
		return [ ord(m[i:i+2].decode("hex")) for i in range(0,len(m),2) ]

def bxor(b1, b2):
		b1 = c2bs(b1)
		b2 = c2bs(b2)
		return [ e1^e2 for e1,e2 in zip(b1,b2) ]

inout = (
		( ("7c2822eb","fdc48bfb",), ("325032a9","c5e2364b" ), ),
		( ("9f970f4e","932330e4",), ("6068f0b1","b645c008" ), ),
		( ("4af53267","1351e2e1",), ("87a40cfa","8dd39154" ), ),
		( ("5f67abaf","5210722b",), ("bbe033c0","0bc9330e" ), ),
)


for e in inout:
		for l in bxor(e[0][0],e[1][0]):
				sys.stdout.write(chr(l).encode("hex"))
		sys.stdout.write('\n')

		for l in bxor(e[1][0],e[1][1]):
				sys.stdout.write(chr(l).encode("hex"))
		sys.stdout.write('\n')
		sys.stdout.write('\n')
