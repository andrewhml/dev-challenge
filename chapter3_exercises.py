# Exercises for chapter 3:

# Name: Andrew Lee

repeat_lyrcis()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

def repeat_lyrcis():
	print_lyrics()
	print_lyrics()

	#Traceback (most recent call last):
			#File "chapter3_exercises.py", line 5, in <module>
		#repeat_lyrcis()
		#NameError: name 'repeat_lyrcis' is not defined

def repeat_lyrcis():
	print_lyrics()
	print_lyrics()		

repeat_lyrcis()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

		  #\Traceback (most recent call last):
  			#File "chapter3_exercises.py", line 24, in <module>
    		#repeat_lyrcis()
			  #File "chapter3_exercises.py", line 21, in repeat_lyrcis
			    #print_lyrics()
			#NameError: global name 'print_lyrics' is not defined

def print_twice(bruce = 'Hello!'):
	print bruce
	print bruce

print_twice('Spam')

def right_justify(allen = 'allen'):
	spaces = 70 - len(allen)
	print " " * spaces + allen

right_justify()


#3.4
1 def print_spam():
	#print 'spam'

do_twice(print_spam)

#NameError: name 'do_twice' is not defined


#2 

def print_spam():
	#print 'spam'

def do_twice(f):
	#f()
	#f()

do_twice(print_spam)

#3

def print_twice():
	print "spam"
	print "spam"

def do_twice(f):
	f()
	f()

do_twice(print_twice)

#4
def print_twice(argument):
	print argument
	print argument

def do_twice(f, argument ):
	f(argument)
	f(argument)

do_twice(print_twice, 'spam' )

#5
def print_function(argument = 'Hello!'):
	print argument

def do_twice(f, argument):
	f(argument)
	f(argument)

def do_four(f, argument):
	do_twice(f, argument)
	do_twice(f, argument)

do_four(print_function, 'Spam')


#3.5
def print_lines():
	print '|', ' '* 9, '|', ' ' * 9, '|'

def print_divider():
	print '+ ', '- ' * 4, '+ ', '- ' * 4, '+'

def four_lines(f):
	f()
	f()
	f()
	f()

def print_box():
	print_divider()
	four_lines(print_lines)
	print_divider()
	four_lines(print_lines)
	print_divider()



