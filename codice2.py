#!/usr/bin/python3
# -*- encoding:utf-8 -*-
d = {}

def div(num):
	ret = []

	if num in d:
		return d[num]
	for i in range(1,num):
		if(num%i==0):
			ret.append(i)

	d[num] = ret
	return ret

def perfetto(num):
	s = 0

	for i in range(1,num):
		if(num%i==0):
			s = s + i

	if s == num:
		return True
	else:
		return False



n = int(input("Inserisci il numero"))
print(div(n)) 
print(perfetto(n))


