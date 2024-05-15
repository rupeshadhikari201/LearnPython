# using single quote
str1 = 'hello, i am rupesh'

# using double quote
str2 = "hello, i am ramesh"

# using tripple single quote
str3 = '''hello, i am ram'''

# using tripple doubel quote
str4 = """hello, i am hanuman"""

# double quote inside single quote
str5 = 'hello, ram is a "god". He is worshiped'

# single quote inside doubel quote
str6 = "hello, hanuman is a 'god'. He is worshiped"

# using escape character
str7  = 'hello i\'m, rupesh'

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)

# Memory Allocation in Python 
str8 = "GeekyShow"
str9 = "GeekyShow"
print("address of {s}".format(s=str8), id(str8))        # both have same memory address
print("address of {s}".format(s=str9), id(str9))

# Mutable and immutable objects in python
'''
Mutabel Objects   : List, Set, Dictionary
Immutable Obejcts : Number, String, Tuple
'''
str10 = 'GeekyShow'
try:
    str[5] = 'R'
except:
    print("String Is Immutable")

# Repetation Operator
str11 = 'R'
print("repetation operator : ", str11*10, sep=" ")

# Concatenation Operator
print("concatenation operator : ", str10+str11)

# Comparison Operator
''' Python Compare strings based on dictionary order'''
str12 = 'ram'
str13 = 'ramesh'
print("comparison between {r1} and {r2} is : ".format(r1=str12,r2=str13), str12 < str13)

# Formating in Python
'''
    1. C Style Formating
    2. format() method
    3. F-String Method
'''

# String Functions
str14 = "Hello, I am Rupesh kumar yadav. I am 23 years old."
# str14 = "Rupesh"
str15 = "     Rupesh     "
str16 = ['Hello,', 'I', 'am', 'Rupesh', 'kumar', 'yadav.', 'I', 'am', '23', 'years', 'old.']
print("swapcase function : ", str14.swapcase())
print("title function : ", str14.title())
print("casefold function : ", str14.casefold())
print("isupper function : ", str14.upper().isupper())
print("islower function : ", str14.lower().islower())
print("istitle function : ", str14.istitle())
print("isdigit function : ", str14.isdigit())           # returns True if the string contains only numeric digits
print("isalpha function : ", str14.isalpha())           # returns True if the string has at least one character and all alphabet
print("isalnum function : ", str14.isalnum())           # returns True if the string has at least one character and all characters in the string are alphanumeric
print("isspace function : ", str14.isspace())
print("---------------------------")
print("without strip : ", str15)
print("l strip       : ", str15.lstrip())
print("r strip       : ", str15.rstrip())
print("strip         : ", str15.strip())
print("---------------------------")
print("replace function : ", str14.replace("Rupesh", "Ramesh"))     # used to replace a sub string in a string with another sub
print("split function   : ", str14.split(sep=" "))                  # is method is used to split/break a string into pieces.
print("join function    : ", " ".join(str16))                  # This method is used to join strings into one string.
print("starts with      : ", str14.startswith("Hello"))
print("ends with        : ", str14.endswith("old."))