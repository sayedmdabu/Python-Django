# Python Global, Local and Nonlocal variables
# Global Variables
"""
In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

Let's see an example of how a global variable is created in Python.
"""
# Example 1: Create a Global Variable


x = "global"


def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

"""
In the above code, we created x as a global variable and defined a foo() to print the global variable x. Finally, we call the foo() which will print the value of x.

What if you want to change the value of x inside a function?
"""

"""
x = "global"


def foo():
    x = x * 2
    print(x)


foo()
"""

# ===========================================
# Local Variables
"""
A variable declared inside the function's body or in the local scope is known as a local variable.
"""
# Example 2: Accessing local variable outside the scope

'''
def foo2():
    a = "local"


foo2()
print(a)

The output shows an error because we are trying to access a local variable y in a global scope whereas the local variable only works inside 'foo()' or local scope.
'''

# Example 3: Create a Local Variable


def foo():
    y = "local"
    print(y)


foo()
# Let's take a look at the earlier problem where x was a global variable and we wanted to modify 'x' inside 'foo()'.

# Example 4: Using Global and Local variables in the same code

x = "global "

print('=============================')


def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


foo()

"""
In the above code, we declare 'x' as a global and 'y' as a local variable in the 'foo()'. Then, we use multiplication operator '*' to modify the global variable 'x' and we print both 'x' and 'y'.

After calling the 'foo()', the value of 'x' becomes 'global global' because we used the 'x * 2' to print two times 'global'. After that, we print the value of local variable 'y' i.e 'local'.
"""

# Example 5: Global variable and Local variable with same name
x = 5

print('==================================')


def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)

"""
In the above code, we used the same name 'x' for both global variable and local variable. We get a different result when we print the same variable because the variable is declared in both scopes, i.e. the local scope inside 'foo()' and global scope outside 'foo()'.

When we print the variable inside 'foo()' it outputs local x: 10. This is called the local scope of the variable.

Similarly, when we print the variable outside the 'foo()', it outputs 'global x: 5'. This is called the global scope of the variable.
"""

# ===============================================
# Nonlocal Variables

'''
Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

Let's see an example of how a global variable is created in Python.

We use nonlocal keywords to create 'nonlocal' variables.
'''

# Example 6: Create a nonlocal variable
print('======================================')
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

'''
In the above code, there is a nested 'inner()' function. We use 'nonlocal' keywords to create a nonlocal variable. The 'inner()' function is defined in the scope of another function 'outer()'.

Note : If we change the value of a nonlocal variable, the changes appear in the local variable.
'''
