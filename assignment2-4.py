#!/usr/bin/env python

import cryptolib as cl

vals = (
		( ("e86d2de2","e1387ae9"),("1792d21d","b645c008",), ),
		( ("7b50baab","07640c3d"),("ac343a22","cea46d60",), ),
		( ("5f67abaf","5210722b"),("bbe033c0","0bc9330e",), ),
		( ("2d1cfa42","c0b1d266"),("eea6e3dd","b2146dd0",), ),
)

for e in vals:
		print cl.msg2bs(e[0][0])
