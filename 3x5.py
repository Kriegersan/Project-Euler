#!/bin/env python

def byThreeFive(a):
	if(a % 3 == 0 or a % 5 == 0):
		return a

def main():

	total = []
	stuff = range(1000)

	for things in stuff:
		total.append(byThreeFive(things))

	st = [x for x in total if x is not None]
	print sum(st)

if __name__ == '__main__':
	main()
