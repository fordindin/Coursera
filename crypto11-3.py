#!/usr/bin/env python

budget = 4*10**12
cost = 200
performance = 1*10**9
keyspace = 2**128

opsperyear = budget/cost*performance*60*60*24*356

print keyspace/opsperyear
