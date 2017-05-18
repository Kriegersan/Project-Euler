#!/usr/bin/evn python

def isMulti(x): # This function tests to see if a number is evenly divisble from 1 to 20
	nope = 0 # setting counters 
	yup = 0
	for y in range(1,21):  # Loops through the division     
		if x % y == 0:   
			yup +=1
		else:
			nope +=1
	if yup == 20:  # see if it passes  all the test returns true
		return True
	else:
		return False
def main():
	
	num = 2520 # setting becaue the number has to be greater than 2520
	while True:
		if num % 20 == 0: # helps to elimiate non contenders 
			hope = isMulti(num)
			if hope:
				break # breaks while loop when Hope is true
		num +=2520 #chances to double the number Incressed speed orig. set to one to be on the safe side 

	print num # print answer 
if __name__ == '__main__':
	main()
