--------Error and Exceptions-------------
In this project we will be diving into errors in python

---Types of Errors---
a) Syntax Errors

>>>	while True print('Hello world')
	File "<stdin>", line 1
		while True print('Hello world')
						^
SyntaxError: invalid syntax

 * The parser repeats the offending line and displays an arrow where the error was detected.
 * The error is caused by the token preceding the arrow
 * in the example above the function print(), a semicolon is missing before it.

b) Exception Errors
 * Are Errors detected during execution and are not conditionally fatal
 * Most exceptptions are not handled by programs and result in error messages as shown below:
	>>> 10 * (1/0)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero
	>>> 4 + spam*3
	Traceback (most recent call last):File "<stdin>", line 1, in <module>
	NameError: name 'spam' is not defined
	>>> '2' + 2
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: can only concatenate str (not "int") to str
 * The last line of the error message shoes what happened.
 * Types:
	- ZeroDivisionError
	- TypeError
	- NameError

---Handling Exceptions---
	while True:
		try:
			x = int(input('Enter a number'))
			break
		except ValueError:
			print("No input")

 * A try clause is executed and if there is no exception the except clause is skipped and the try clause is finished
 * if an exception occurs, the rest of the try is skipped and the except clause is executed if its type matches the value named after the except.
 * if an exception occurs but does not match the provided types in the except, it is passed on to try statements , and it becomes an unhandled execption.
 * A try statement can have more than one except clause.
	>>> except (RuntimeError, TypeError, NameError):
			pass
 * When an exception occurs, it may have associated values, also known as the exception’s arguments. The presence and types of the arguments depend on the exception type.
 * Exception handlers do not handle only exceptions that occur immediately in the try clause, but also those that occur inside functions that are called (even indirectly) in the try clause.
	>>> def this_fails():
			x = 1/0
			
	>>> try:
			this_fails()
		except ZeroDivisionError as err:
			print('Handling run-time error:', err)
		
		Handling run-time error: division by zero

---Raising Exceptions---
 * The raise statement allows the programmer to force a specified exception to occur
	>>> raise NameError('HiThere')
	Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
	NameError: HiThere
 * If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception.

---Exception Chaining---
 * If an unhandled exception occurs inside an except section, it will have the exception being handled attached to it and included in the error message
 * To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause
	raise RuntimeError from exc
