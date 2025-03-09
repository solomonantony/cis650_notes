# files_notes
# File I/O using Python
- Data maintained in files is persistent
- Computers store files on secondary storage devices
- solid-state drives, hard disks, and more
- We consider text files in several popular formats
# Some file types
- plain text (see details)
- JSON (JavaScript Object Notation) (see example)
- CSV (comma-separated values) (see example)
- Fixed width format (see example)
# File
- A text file is a sequence of characters
- A binary file (for images, videos and more) is a sequence of bytes
- First character in a text file or byte in a binary file is located at position 0
- In a file of n characters or bytes, the highest position number is n – 1
- For each file you open, Python creates a file object that you’ll use to interact with the file
# End of File
- Every operating system provides a mechanism to denote the end of a file (EOF)
- Some use an end-of-file marker
- Others maintain a count of the total characters or bytes in the file
- Programming languages hide these operating-system details from you
# Standard File Objects
- When a Python program begins execution, it creates three standard file objects:
- sys.stdin—the standard input file object
- sys.stdout—the standard output file object, and
- sys.stderr—the standard error file object.
- Though considered file objects, they do not read from or write to files by - default
- The input function implicitly uses sys.stdin to get user input from the keyboard
- Function print implicitly outputs to sys.stdout, which appears in the command line
- Python implicitly outputs program errors and tracebacks to sys.stderr, which also appears in the command line
- Import the sys module if you need to refer to these objects explicitly in your code—this is rare.
# File-open modes
- 'r' ==> Open for reading; default mode when you don't specify any more
- 'w' ==> Open a text file for writing; existing file contents are deleted
- 'a' ==> Open a text file for creating or append to existing file
- 'w+' ==> Open a file for reading and writing. existing file contents are deleted
- 'a+' ==> Open for reading and appending
# File Object Methods
## read
- For a text file, returns a string containing the number of characters specified by the method’s integer argument
- For a binary file, returns the specified number of bytes
- If no argument is specified, the method returns the entire contents of the file
## readline
- Returns one line of text as a string, including the newline character if there is one
- Returns an empty string when it encounters the end of the file
## writelines
- Receives a list of strings and writes its contents to a file
## json format
- JSON (JavaScript Object Notation) is a text-based, human-and-computer-readable, data-interchange format used to represent objects as collections of name–value pairs.
- Preferred data format for transmitting objects across platforms.
- Similar to Python dictionaries
- Each JSON object contains a comma-separated list of property names and values, in curly braces.
- JSON arrays, like Python lists, are comma-separated values in square brackets.
- Copy the contents on right and create a text file (named example.json) on your computer - in the same folder as your script.
## Deserializing the JSON Text
- json module’s load function reads entire JSON contents of its file object argument and converts the JSON into a Python object
- Known as deserializing the data
- json module’s dumps function (dumps is short for “dump string”) returns a Python string representation of an object in JSON format
- Can be used to display JSON in a nicely indented format (sometimes called “pretty printing”)
- When call includes the indent keyword argument, the string contains newline characters and indentation for pretty printing.  Also can use indent with the dump function when writing to a file
## csv module
- csv module provides functions for working with CSV files
- csv module’s documentation recommends opening CSV files with the additional keyword argument newline='' to ensure that newlines are processed properly
- .csv file extension indicates a CSV-format file
- writer function returns an object that writes CSV data to the specified file object
- writer’s writerow method receives an iterable to store in the file
- By default, writerow delimits values with commas, but you can specify custom delimiters
## Reading from a CSV File
- Read records from the file accounts.csv and display the contents of each record
- csv module’s reader function returns an object that reads CSV-format data from the specified file object
- Can iterate through the reader object one record of comma-delimited values at a time
