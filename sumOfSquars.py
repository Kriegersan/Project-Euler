#!/usr/bin/env python


def main():

	setX = range(1,101) # setting the range from 1 to 100
	sfSquares = [] # empty list to add all the squares from 1 to 100
	for y in setX:
		sfSquares.append(y**2) 
	print sum(sfSquares) # printing for show the sum of all the squares 1 to 100

	sSetX = sum(setX) #Taking the sum of 1 to 100

	total = sSetX**2 # squaring the sum of 1 to 100

	print total # print for show the total of the sum squared

	diff = total - sum(sfSquares) # taking the difference 

	print diff # done!

if __name__ == '__main__':
	main()