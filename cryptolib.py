#!/usr/bin/env python

def msg2bs(m):
		return [ m[i:i+2] for i in range(0,len(m),2) ]

def sxor(a,b):
		a,b = msg2bs(a)[:len(targetbs)],msg2bs(b)[:len(targetbs)]
		return [ chr(ord(x1.decode("hex"))^ord(x2.decode("hex"))).encode("hex") for x1,x2 in zip(a,b) ]
