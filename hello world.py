Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("helloworld")
helloworld
>>> print ("change 1")
change 1
>>> def change
SyntaxError: invalid syntax
>>> def change:
	
SyntaxError: invalid syntax
>>> def change()
SyntaxError: invalid syntax
>>> def change():
	print("change/n")

	
>>> change()
change/n
>>>  def change():
	print("change\n")
	
SyntaxError: unexpected indent
>>> def change():
	print("change\n")

	
>>> change()
change

>>> 