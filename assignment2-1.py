#!/usr/bin/env python

import math
events = {
				math.pow(2,128) :1 ,
				math.pow(10,6) :2 ,
				math.pow(10,30) :3,
				math.pow(10,36) :4,
				math.pow(10,42) :5,
		}

klist = events.keys()
klist.sort()

for k in klist:
		print events[k]
