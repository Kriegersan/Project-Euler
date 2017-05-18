#!/bin/env python

#This function checks if a number is a palindrome 
def palCheck(number): 
	temp = number
	rev = 0 # setting the revrse = 0 
	while temp is not 0:  # looping over the number to reverse it 
		rev = rev * 10
		rev = rev + temp % 10
		temp /= 10

	if number == rev:  # checking with value of revrse is true 
		return True

def main():

	list = []

	for x in range(100,1000):
		for y in range(100,1000):
			myPal = x*y
			if palCheck(myPal):
				list.append(myPal)

	print max(list)

if __name__ == '__main__':
	main()
