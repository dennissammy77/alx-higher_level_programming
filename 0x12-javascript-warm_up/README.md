/**********Javascript***********/

_Variables_
Variables are containers that store values.

Data_Types
String-This is a sequence of text known as a string. To signify that the value is a string, enclose it in single or double quote marks.

Number-This is a number. Numbers don't have quotes around them.

Boolean-This is a True/False value. The words true and false are special keywords that don't need quote marks.

Array-This is a structure that allows you to store multiple values in a single reference.

Object-This can be anything. Everything in JavaScript is an object and can be stored in a variable.

_Comments_
Comments are snippets of text that can be added along with code. The browser ignores text marked as comments.

i.e 
// or /* */ can be used to show the begining and end of comment.

_Operators_

_Conditionals_
Conditionals are code structures used to test if an expression returns true or not.
A very common form of conditionals is the if...else statement.

_Functions_
Functions are a way of packaging functionality that you wish to reuse.
It's possible to define a body of code as a function that executes when you call the function name in your code. 
This is a good alternative to repeatedly writing the same code.
Functions often take arguments: bits of data they need to do their job.
Arguments go inside the parentheses, separated by commas if there is more than one argument.

_Events_
Real interactivity on a website requires event handlers. 
These are code structures that listen for activity in the browser, and run code in response.
The most obvious example is handling the click event, which is fired by the browser when you click on something with your mouse.

__Data Types__
_Null type_
The Null type is inhabited by exactly one value: null.

_Undefined type_
The Undefined type is inhabited by exactly one value: undefined.
Undefined indicates the absence of a value, while null indicates the absence of an object.
The language usually defaults to undefined when something is devoid of a value:
	- A return statement with no value (return;) implicitly returns undefined.
	- Accessing a nonexistent object property (obj.iDontExist) returns undefined.
	- A variable declaration without initialization (let x;) implicitly initializes the variable to undefined.
	- Array.prototype.find() and Map.prototype.get(), return undefined when no element is found.
null is a keyword, but undefined is a normal identifier that happens to be a global property. 
In practice, the difference is minor, since undefined should not be redefined or shadowed.

_Boolean type_
The Boolean type represents a logical entity and is inhabited by two values: true and false.
Boolean values are usually used for conditional operations, including ternary operators, if...else, while, etc.

_Number type_
The Number type is a double-precision 64-bit binary format IEEE 754 value.

_BigInt type_
The BigInt type is a numeric primitive in JavaScript that can represent integers with arbitrary magnitude. With BigInts, you can safely store and operate on large integers even beyond the safe integer limit (Number.MAX_SAFE_INTEGER) for Numbers.
