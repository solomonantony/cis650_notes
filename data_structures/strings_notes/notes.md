## Introduction

- A string contains a sequence of characters
- String literals are enclosed on single or double quotes
- Use backslash escape characters to show a quote inside a string literal
- String operations are used in 
    - Anagrams
    - Automated grading of written homework
    - Automated teaching systems
    - Categorizing articles
    - Chatbots
    - Compilers and interpreters
    - Creative writing
    - Cryptography
    - Document classification
    - Document similarity
    - Document summarization
    - Electronic book readers
    - Fraud detection
    - Grammar checkers
    - Inter-language translation
    - Legal document preparation
    - Monitoring social media posts
    - Natural language understanding
    - Opinion analysis
    - Page composition software
    - Palindromes
    - Parts-of-speech tagging
    - Project Gutenberg free books
    - Reading books, articles, documentation and absorbing knowledge
    - Search engines
    - Sentiment analysis
    - Spam classification
    - Speech-to-text engines
    - Spell checkers
    - Steganography
    - Text editors
    - Text-to-speech engines
    - Web scraping
    - Word clouds
    - Word games
    - Writing medical diagnoses from x-rays, scans, blood tests
    - and many more…
##  String literals

- Digital representation of text
- The ASCII codes used 7 bits ==> 128 distinct values
- ASCII character encoding (e.g. ASCII 65 => A, 66 => B etc.)
- See https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/1280px-ASCII-Table-wide.svg.png


- Literal is a value assigned to a variable
- String literals are enclosed on single or double quotes
- "This is a string - 1223 [xy019]"
- Use backslash escape characters to show a quote inside a string literal
- 'This string's escape character is \'
- A string literal can span multiple lines, but there must be a backslash \ at the end of each line to escape the newline.
- Multiline string can be placed within triple quotes as well
- Python's encoding is UTF-8. You can use the ALT+224 to print α, ALT+225 to print ß ALT+226 to print Γ etc. See https://usefulshortcuts.com/downloads/ALT-Codes.pdf for other ALT codes.
- Each alphabet and number and other printable characters have a Unicode code
- Use the chr() function to return the Unicode character represented

```
string1 = "This is a string - 12'23' [xy019]"
string2 = 'This string\'s escape character is \\'
print(string2)
```

```
string4 = """
           This is an example of a
           multi-line string.  It spans
           many lines"""
print(string4)
```
```
print(chr(0x1F60E))  #see https://unicode.org/Public/emoji/13.0/emoji-sequences.txt other emojis
ord('b')
```

```
"\N{GREEK SMALL LETTER DELTA}"
```
```
#print the lower case alpha using the \N
"\N{GREEK SMALL LETTER ALPHA}"
```
## String methods

```
stuff = "heLlo, world"
#help(str) # to view the list of methods
```

```
help(dir(str))
```

```
stuff.capitalize()
stuff.upper()
stuff.lower()
stuff.title()
stuff.swapcase() == stuff
stuff.casefold()
```

```
stuff2 = "Hello\tworld"
print(stuff2)
stuff2.expandtabs(tabsize=8)
```

```
"string with space   ".rstrip()
"    string with space   ".lstrip()

```
```
stuff.replace('l', 'g')
```

```
"Dr. Smith".removeprefix("Dr. ")
```

```
"John Jr.".removesuffix("Sr.")
```

```
stuff.center(20,'_')
'Be'.ljust(4, 'x')
```

```
"$3,489.22".rjust(20,'.')
```
```
"43".zfill(5)
```

```
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```
## Methods for searching within strings

```
"goooooggggle yourself".count('g')
```
```
"goooooggggle yourself".find('g')
"goooooggggle yourself".rfind('g')
```
```
"google yourself".index('g')
```
```
print("google yourself".index('o'))
"google yourself".rindex('o')
```
## Methods for joining and splitting strings

```
'_'.join(['ab', 'pq', 'rs'])
```

```
print("google yourself".index('o'))
"google yourself".rindex('o')
```

```
stuff.partition('o')
```

```
"how are you?".split()
```

```
stuff.rsplit('o')
```

```
stuff2 = """
The world is blasting through climate records as scientists sound the alarm:
The likelihood is growing that 2023 could be the hottest year on record,
and the climate crisis could be altering our weather in ways they don’t yet understand.

And they are not holding back – “extraordinary,” “terrifying” and “uncharted
territory” are just a few of the ways they have described the recent spike in
global temperature
"""
len(stuff2.splitlines())
```
## Inspecting strings

-isalnum() ''==> are all characters letters or digits?
- isalpha() ''==> are all characters letters?
- isdigit() ''==> are all characters digits (0, 1, …, 9)?
- isidentifier() ''==> is the string a valid Python identifier, e.g., could it be used as a variable name?
- islower() ''==> are the characters lowercase letters (a, b, …, z)?
- isspace() ''==> are the characters all whitespace characters?
- isupper() ''==> are the characters uppercase letters (A, B, …, Z)?

## String conversions

- int() and float() can convert strings containing numbers to numbers
- str() can be used to convert numbers (and other types) to strings
  - Useful for concatenating numbers with strings
- format() can be used to convert a number to a formatted string

## String comparisons
- Strings can be compared for equality (same sequence of characters) with ==
- Compare for inequality with !=
- Other string comparisons: < > <= >=

```
name1 = 'Steve'
name2 = 'Stevie'
name1 < name2
"ABC" > "abc"
```

# String slices

- String slices are substrings extracted from a larger string
- To extract a single charcter, use its index inside brackets
- Index 0 is for the first character
- Index -1 is for the last character

```
# Strings are similart to lists
# individual characters in a string can be accessed using the index
alphabets = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabets))
print(alphabets[1])
```
- Slicing is done by specifying the index of the start and end positions separated by a : inside brackets[]
- If the end position is after the start position, the characters in between are returned

```
start = int(input("Enter a start position: "))
stop = int(input("Enter a stop position: "))
print(alphabets[start:stop])
```
- In addition to the start and stop, we can specify the step also to skip a number of characters
- If stop > start, and step = 1, it will return all the characters betwee start and stop
- If start < stop and step <0, it will return the characters in reverse order
```
start = int(input("Enter a start position: "))
stop = int(input("Enter a stop position: "))
step = int(input("Enter step number: "))
print(alphabets[start:stop:step])
```

- If the start position is not given, it will use 0 as start
- If the stop position is not given, it will use the end of string the as stop

```
alphabets[-5:]
```
- If neither start or stop is given, and step is -1, it will return the reverse of the string

```
alphabets[::-1]
```

```
#to get first 3 characters
alphabets[:3]
```
```
#to get last 3 characters
alphabets[-3:]
```

## String module

- Useful for accessiong string string constants

```
import string
```

```
print(string.ascii_letters)
print()
print(string.ascii_lowercase)
print()
print(string.ascii_uppercase)
print()
print(string.digits)
print()
print(string.octdigits)
print()
print(string.whitespace)
print()
print(string.punctuation)
print()
print(string.printable)

```
## Custom formatting

```
a,b,c,d = 10,11,12,13
f'{65:c} {97:c}'
```

```
a,b,c,d = 10,11,12,13
print('{} {}'.format(a,b))
print()
print('{0} {1}'.format(a,b))
print()
print(f'{a} {c}')
print()
print(f'{a} {c}')
print()
print(f'{a:>10}')
print()
print(f'{a:<10}')
print()
print(f'{a:x>3}')
print()
print(f'{a:x^10}')
```
## Concatenating

```
s1 = 'happy'
s2 = 'birthday'
s1 += s2
s1
```


