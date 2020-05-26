# Python Data Types
"""
Data types in Python
Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.
"""
# Python Numbers
"""
Integers, floating point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.

We can use the type() function to know which class a variable or a value belongs to. Similarly, the isinstance() function is used to check if an object belongs to a particular class.
"""
a = 5
print(a, "is of type", type(a))

b = 2.0
print(b, "is of type", type(b))

c = 1 + 2j
print(c, "is complex number?", isinstance(1 + 2j, complex))

"""
Integers can be of any length, it is only limited by the memory available.

A floating-point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points. 1 is an integer, 1.0 is a floating-point number.

Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part. Here are some examples.
"""
a = 1234567890123456789
print(a)

d = 0.1234567890123456789
print(d)

c = 1 + 3j
print(c)

""" Notice that the float variable b got truncated. """


# Python List
"""
List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].

We can use the slicing operator [ ] to extract an item or a range of items from a list. The index starts from 0 in Python.
"""
a1 = [5, 10, 15, 20, 25, 30, 35, 40]

# a1[2] = 15
print("a1[2] = ", a1[2])

# a[0:3] = [5, 10, 15]
print("a1[0:3] = ", a1[0:3])

# a[5:] = [30, 35, 40]
print("a1[5:] = ", a1[5:])


# Python Tuple
"""
Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

It is defined within parentheses () where items are separated by commas.

We can use the slicing operator [] to extract items but we cannot change its value.
"""
t = (5, 'program', 1 + 3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10


# Python Set
"""
Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.
"""
a = {5, 2, 3, 1, 4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

"""
We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.
"""
a = {1, 2, 2, 3, 3, 3}
print(a)

"""
Since, set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.
"""

# Python Dictionary

"""
Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

In Python, dictionaries are defined within braces {} with each item being a pair in the form 'key:value'. Key and value can be of any type.

We use key to retrieve the respective value. But not the other way around.
"""

d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
# print("d[2] = ", d[2])


# Conversion between data types
"""
We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.

Conversion from float to int will truncate the value (make it closer to zero).
"""
print(float(5))
print(int(10.6))
print(int(-10.6))

# Conversion to and from string must contain compatible values.
print(float('2.5'))
print(str(25))

# We can even convert one sequence to another.
print(set([1, 2, 3]))
print(tuple({5, 6, 7}))
print(list('hello'))

# To convert to dictionary, each element must be a pair:
print(dict([[1, 2], [3, 4]]))
print(dict([(3, 26), (4, 44)]))
