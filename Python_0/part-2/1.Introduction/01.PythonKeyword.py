# List of Keywords in Python
# Keywords are the reserved words in Python. We cannot use a keyword as variable name, function name or any other identifier.
# Here's a list of all keywords in Python Programming.
# You Can always get the list of keywords in your current version by typing the following in the prompt.
import keyword
print(keyword.kwlist)

# ========================================================
# Description of Keywords in Python with examples
# True, False
# "True" and "False" are truth values in Python. They are the results of comparison operations or logical (Boolean) operations is Python. For example:
print(1 == 1)
# True
print(5 > 3)
# True
print(True or True)
# True
print(10 <= 1)
# False
print(3 > 7)
# False
print(True and False)
# False

# Here we can see that the first three statements are true so the interpreter returns "True" and returns "False" for the remaining three statements. "True" and "False" in Python is same as "1 and 0". This can be justified with the following example:
print(True == 1)
# True
print(False == 0)
# True
print(True + True)
# 1 +1 = 0

# ========================================================
# None
# "None" is a special constant in Python that represents the absence of a value or a null value.
# It is an object of Its own database, the "NoneTyp"e. We cannot create multiple "None" objects but can assign it to variables. These variables will be equal to one another.
# We must take special care that "None" does not imply "False, 0" or any empty  list dictionary, string etc. For example:
print(None == 0)
# False
print(None == [])
# False
print(None == False)
# False
x = None
y = None
print(x == y)
# True

# Void function that do not anything will return a "None" object automatically. "None" is also returned by function in which the program flow does not encounter a return statement. For example:


def a_void_function():
    a = 1
    b = 2
    c = a + b


x = a_void_function()
print(x)

# This program has a function that does not return a value, although it does some operations inside. So when we print "x", we get "None" what returned automatically (implicitly). Similarly, here is another example:


def imroper_return_funtcion(a):
    if (a % 2) == 0:
        return True


x = imroper_return_funtcion(4)
print(x)
# Although this function has a "return" statement, it is not reached in every case. The function will return "True" only when the input is even.
# If we give the function an odd number, "None" is returned implicitly.

#========================================================
# and, or, not
# "and", "or" "not" the logical operators in Python. "and" will result into "True" only if both the operands are True. For example:
print(True and False)
# False
print(True or False)
# True
print(not False)
# True

# ========================================================
# as
# as is used to create an alias while importing a module. It means giving a different name (user-defined) to a module while importing it.
# As for example, Python has a standard module called "math". Suppose we want to calculate what cosine pi is using an alias. We can do it as follows using "as":
import math as myAlias
print(myAlias.cos(myAlias.pi))
# Here we imported the "math" module by giving it the name "myAlias". Now we can refer to the "math" module with this name. Using this name we calculated cos(pi) and got "-1.0" as the answer.

# ========================================================
# assert
#"assert" is used for debugging purposes.
# While programming, sometimes we wish to know the internal state or check if our assumptions are true. "assert" helps us do this and find bugs more conveniently. "assert" is followed by a condition.
# If the condition is true, nothing happens. But if the condition is false, "AssertionError" is raised. For example:
# a = 4
# assert a<5
# assert a>5
# Traceback (most recent call last):
#   File "<string>", line 301, in runcode
#   File "<interactive input>", line 1, in <module>
# AssertionError: The value of a is too small

# For our better understanding, we can also provide a message to be printed with the "AssertionError".

# a = 4
# assert a > 5, "The value of a is too small"
# Traceback (most recent call last):
#   File "<string>", line 301, in runcode
#   File "<interactive input>", line 1, in <module>
# AssertionError: The value of a is too small

# At this point we can note that,
# assert condition, message
# is equivalent to,
# if not condition:
#     raise AssertionError(message)


# ========================================================
# async, await
#
