# functions_notes
Function is a device that groups a set of statements so that they can be run more than once in a program.

for maximizing code reuse,

Functions are the alternative to programming by copy-and-paste — rather than having multiple redundant copies of an operation’s code, we can factor it into a single function.

Python functions are the most basic factoring tool in the language Functions are also used for splitting systems into pieces that have well defined roles.

Why use functions?
Construct large programs from smaller, more manageable pieces.
Divide and conquer.
Use existing functions as building blocks.
Key aspect of software reusability.
Also a major benefit of object-oriented programming.
Packaging code as a function allows you to execute it from various locations in your program just by calling the function.
Makes programs easier to modify.

The def statement
def is an executable statement, like if, while, for, and so on.
def creates an object and assigns it to a name. The function name becomes a reference to the function object.
By convention function names should begin with a lowercase letter and in multiword names underscores should separate each word.
Required parentheses contain the function’s parameter list. a.k.a. arguments
Empty parentheses mean no parameters.

Parameters or Arguments
Parameters are inputs for a function
Parameters exist only during the function call. Created on each call to the function to receive arguments.
Destroyed when the function returns its result to the caller.
A function’s parameters and variables defined in its block are all local variables.

Arguments
When calling functions, you can use keyword arguments to pass arguments in any order.

Default Parameter Values:
Default Parameter Values: if you omit the argument for a parameter with a default parameter value, the default value for that parameter is automatically passed.

Arbitrary Argument Lists
Functions with arbitrary argument lists, such as built-in functions min and max, can receive any number of arguments.

Function min's documentation states that min has two required parameters (named arg1 and arg2) and an optional third parameter of the form *args, indicating that the function can receive any number of additional arguments.

The * before the parameter name tells Python to pack any remaining arguments into a tuple that’s passed to the args parameter.


Return statement
return sends a result object back to the caller. The Python return statement can show up anywhere in a function body; when reached, it ends the function call and sends a result back to the caller.

The return statement consists of an optional object value expression that gives the function’s result. If the value is omitted, return sends back a None.

yield statement
yield sends a result object back to the caller, but remembers where it left off.

Yield statement is turned into a generator function with its iterator with automatic retention of its local scope and code position.

Passing functions as objects
It is legal to nest a function def inside an if statement to select between alternative definitions:

One way to understand this code is to realize that the def is much like an = statement: it simply assigns a name at runtime.

Overloading of functions
Python functions can perform differently depending on the data types of the arguments

Factory function
Way to create a function; function that creates and returns another function,

Lambda functions
It is an expression that generates a new function to be called later, much like a def statement.

Because it’s an expression, though, it can be used in places that def cannot, such as within list and dictionary literals. lambda’s body is a single expression, not a block of statements.

The lambda expression, a feature that allows us to inline function definitions.

Functions with no names.


Built-in functions
Python’s Built-In max and min Functions For other built-in functions, review https://docs.python.org/3/library/functions.html

Python Standard Library
Standard library contains numerous functions that are already written

You write Python programs by combining functions and classes (that is, custom types) that you create with pre-existing functions and classes defined in modules, such as those in the Python Standard Library and other libraries.

Avoid “reinventing the wheel.”

A module is a file that groups related functions, data and classes.

A package groups related modules.

The Python Standard Library is provided with the core Python language. See https://docs.python.org/3/library/


