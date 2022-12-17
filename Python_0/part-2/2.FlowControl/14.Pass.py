# Python pass statement
# What is pass statement in Python?
"""
In Python programming, the 'pass' statement is a null statement. The difference between a comment and a 'pass' statement in Python is that while the interpreter ignores a comment entirely, 'pass' is not ignored.

However, nothing happens when the 'pass' is executed. It results in no operation (NOP).

Syntax of pass
pass

We generally use it as a placeholder.

Suppose we have a 'loop' or a 'function' that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would give an error. So, we use the 'pass' statement to construct a body that does nothing.
"""
'''pass is just a placeholder for
functionality to be added later.'''

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
