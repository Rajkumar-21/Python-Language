# Printing String

a="Hello World"
print(a)

# String Indexing
print(a[2])    # Prints 2 index of 'a' variable

# Slicing [start:stop:jump]
print(a[::])

print(a[1:])

print(a[:2])

print(a[::2])

print(a[-1])

print(a[::-1])  # prints in reverse

# string is immutable so we can do concatenation 

a = a + ' this adds to my string !'

print(a)

# we can multiply the string

let = 'Raj \t'

print(let * 3)  # prints 3 times

print(a.upper())  # makes all the string in capital

print(a.split())  # splits by whitespace in a list

print(a.split('i'))