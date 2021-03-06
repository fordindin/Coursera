#!/usr/bin/env python
import sys
#k = [ '0011', '1111', '0101', '1100', '0001' ]

kcc = ['0b1010', '0b100', '0b1', '0b1000', '0b1']
kset = [['0b1010', '0b1110', '0b1011', '0b10', '0b1011'], ['0b1010', '0b1110', '0b1011', '0b10', '0b1011'], ['0b1010', '0b1100', '0b1001', '0b0', '0b1001'], ['0b1010', '0b1100', '0b1001', '0b0', '0b1001'], ['0b1010', '0b101', '0b0', '0b1001', '0b0'], ['0b1010', '0b101', '0b0', '0b1001', '0b0'], ['0b1010', '0b101', '0b0', '0b1001', '0b0'], ['0b1010', '0b1111', '0b1010', '0b11', '0b1010'], ['0b1010', '0b1111', '0b1010', '0b11', '0b1010'], ['0b1010', '0b1010', '0b1111', '0b110', '0b1111'], ['0b1010', '0b1010', '0b1111', '0b110', '0b1111'], ['0b1010', '0b111', '0b10', '0b1011', '0b10'], ['0b1010', '0b111', '0b10', '0b1011', '0b10'], ['0b1010', '0b1', '0b100', '0b1101', '0b100'], ['0b1010', '0b1', '0b100', '0b1101', '0b100'], ['0b1010', '0b1011', '0b1110', '0b111', '0b1110'], ['0b1010', '0b1011', '0b1110', '0b111', '0b1110'], ['0b1010', '0b110', '0b11', '0b1010', '0b11'], ['0b1010', '0b110', '0b11', '0b1010', '0b11'], ['0b1010', '0b11', '0b110', '0b1111', '0b110'], ['0b1010', '0b11', '0b110', '0b1111', '0b110'], ['0b1010', '0b10', '0b111', '0b1110', '0b111'], ['0b1010', '0b10', '0b111', '0b1110', '0b111'], ['0b1010', '0b1101', '0b1000', '0b1', '0b1000'], ['0b1010', '0b1101', '0b1000', '0b1', '0b1000'], ['0b1010', '0b0', '0b101', '0b1100', '0b101'], ['0b1010', '0b0', '0b101', '0b1100', '0b101'], ['0b1010', '0b1001', '0b1100', '0b101', '0b1100'], ['0b1010', '0b1001', '0b1100', '0b101', '0b1100'], ['0b1010', '0b1000', '0b1101', '0b100', '0b1101'], ['0b1010', '0b1000', '0b1101', '0b100', '0b1101'], ['0b1010', '0b100', '0b1', '0b1000', '0b1'], ['0b1010', '0b100', '0b1', '0b1000', '0b1']]
k = [ '0b1010', '0b101', '0b0', '0b1001', '0b0' ]
xm = [ '0110', '0101', '1110' ] #, '1101' ]
xc = [ '0011', '1010', '0110' ]

def F(k, x):
		try:
				t = int(k[0], 2)
		except TypeError:
				print k[0]
				sys.exit(0)
		xors = [0]
		for i in range(1,5):
				if x[i-1] == '1':
						xors.append(i)
						t = t^int(k[i],2)
		return bin(t)


for i in range(len(xm)):
		if F(k, xm[i]) != bin(int(xc[i],2)):
				print "Fail"


print F(k, '1101')
sys.exit(0)
acc = {}
for k in kset:
		for i in range(len(xm)):
				if F(k, xm[i]) != bin(int(xc[i],2)): break
				else:
						acc.setdefault(tuple(k),0)
						acc[tuple(k)]+=1

print acc

"""
				'1': bin(int(xc[0],2)),
				'2': bin(int(xc[1],2)),
				'3': bin(int(xc[2],2)),
				"""
xor_combos = {
				'0x1': bin(int(xc[0],2)^int(xc[1],2)),
				'0x2': bin(int(xc[0],2)^int(xc[2],2)),
				'1x2': bin(int(xc[1],2)^int(xc[2],2)),
				'0x1x2': bin(int(xc[0],2)^int(xc[1],2)^int(xc[2],2)),
				}

"""
for s in xc:
		#print bin(F(k,s)[0])
		print F(k,s)[1]
"""

def keywalk():
		out = []
		for i in range(pow(2,4)):
				out.append(bin(i))
		return out

candidates = {}

keymap = {
				'0x1':'2x3',
				'0x2':'1x4',
				'1x2':'1x2x3x4',
				'0x1x2':'0x1x2',
				}

counter = 0
for k0 in keywalk():
		for k1 in keywalk():
				for k2 in keywalk():
						for k3 in keywalk():
								for k4 in keywalk():
										counter +=1
										if int(k2,2)^int(k3,2) == int(xor_combos['0x1'],2):
												candidates.setdefault('2x3',[])
												candidates['2x3'].append((k2,k3,))
										if int(k1,2)^int(k4,2) == int(xor_combos['0x2'],2):
												candidates.setdefault('1x4',[])
												candidates['1x4'].append((k1,k4,))
										if int(k1,2)^int(k2,2)^int(k3,2)^int(k4,2) == int(xor_combos['1x2'],2):
												candidates.setdefault('1x2x3x4',[])
												candidates['1x2x3x4'].append((k1,k2,k3,k4))
										if int(k0,2)^int(k1,2)^int(k2,2) == int(xor_combos['0x1x2'],2):
												candidates.setdefault('0x1x2',[])
												candidates['0x1x2'].append((k0,k1,k2))

candidates['2x3'] = set(candidates['2x3'])
candidates['1x4'] = set(candidates['1x4'])
candidates['1x2x3x4'] = set(candidates['1x2x3x4'])
candidates['0x1x2'] = set(candidates['0x1x2'])

c1234_norm_23 = set([ (c[1],c[2],) for c in candidates['1x2x3x4']])
c1234_norm_14 = set([ (c[0],c[3],) for c in candidates['1x2x3x4']])

best_23_candidates = c1234_norm_23.intersection(candidates['2x3'])
best_14_candidates = c1234_norm_14.intersection(candidates['1x4'])


tc = []
for c23 in best_23_candidates:
		for c14 in best_14_candidates:
				if (c14[0], c23[0], c23[1], c14[1],) in candidates['1x2x3x4']:
						tc.append((c14[0], c23[0], c23[1], c14[1],))

tc1 = []
for t in tc:
		for c012 in candidates['0x1x2']:
				if (c012[1], c012[2],) == (t[0],t[1]):
						tc1.append((c012[0],t[0],t[1],t[2],t[3],))

retval = []
for k in tc1:
		for m in xm:
				if F(k, m) != bin(int(xc[xm.index(m)], 2)):
						break
				else:
						retval.append(list(k))
						

print retval

"""
sys.exit(0)


final_candidates = []
for c0 in kc0:
		for c1 in kc1:
				for c2 in kc2:
						if bin(int(c0,2)^int(c1,2)^int(c2,2)) == xor_combos['0x1x2'] and \
										(c0,c1,) in candidates['0x1'] and \
										(c1,c2,) in candidates['1x2']:
								final_candidates.append((c0,c1,c2,))

#print final_candidates

kcopy = list(kcc)

for mk in keywalk():
		kcc[4] = mk
		print mk
		if F(kcc, xm[0]) == bin(int(xc[0], 2)):
				print kcc[4]

#print F(kcopy, xm[2]) == bin(int(xc[2], 2))
#print bin(int(xc[2],2))
"""
