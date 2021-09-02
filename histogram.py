#!/usr/bin/python3

import sys

total = 0
res = list()
for l in sys.stdin.readlines():
	wordc = l.split()
	res.append((wordc[0],int(wordc[1])))
	total += int(wordc[1])
	
for w,c in res:
	print(w.ljust(15),"\t[",sep='',end='')
	for i in range(0,c*100//total,5):
		print("*",sep='',end='')
	print("] ",c*100//total,"%",sep='')
