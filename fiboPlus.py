#!/bin/env python


def fib(x):
	if(x < 2):
		return x

	else:
		return fib(x - 1) + fib(x -2)

     
def main():

	list = 0
	val = 0
	while (fib(val) < 4000000):
		a = fib(val)
		if (a % 2 == 0):
			list += a
		val += 1

	print list


if __name__ == '__main__':
	main()
