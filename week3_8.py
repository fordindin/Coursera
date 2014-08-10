#!/usr/bin/env python

import Crypto.Cipher.AES as AES

def strxor(s1, s2):
		return ''.join([ chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])

'60f2e61be959b0f7e48f9098e7bf10e6'
'66e94bd4ef8a2c3b884cfa59ca342b2e'
'00000000000000000000000000000000'
'00000000000000000000000000000000'

