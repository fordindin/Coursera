#!/usr/bin/env python

def msg2bs(m, blocksize=1):

		return [ m[i:i+blocksize*2] for i in range(0,len(m),blocksize*2) ]

def sxor(a,b):
		a,b = msg2bs(a),msg2bs(b)
		return [ chr(ord(x1.decode("hex"))^ord(x2.decode("hex"))).encode("hex") for x1,x2 in zip(a,b) ]

def hex2data(h):
		return "".join([chr(int(c, 16)) for c in msg2bs(h)])

def data2hex(d):
		return "".join(["{0:02x}".format(ord(c)) for c in d ])
