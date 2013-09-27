# Exercises for chapter 2:

# Name: Andrew Lee

#2.1 
	#The invalid token is due to python interpreting the zicode as a octal number.
	# The number 9 in 02492 is not recognized in a base 8 number system
	# I think the zipcode should be represented as a string

#2.2
	print 5
	x = 5
	print x +1

#2.3
	#8 <type 'int'>
	#8.5 <type 'float' >
	#4.0 <type 'float'>
	#11 <type 'int'>
	#'.....' <type 'str'

#2.4
	#1
	pi = 3.141592653589793
	r = 5
	(4* pi * (r**3))/3
	523.5987755982989

	#2
	n = 60
	(.6 * 24.95)*n + ((n-1) * .75) + 3
	945.4499999999999

	#3
	easypace = 8.25
	tempo = 7.2
	(2 * easypace) + (3 * tempo)
	38.1
	#Convert to minutes 0:38:06 + 6:52:00 7:30:06
	#There is probably a better way to do the converstion and addition