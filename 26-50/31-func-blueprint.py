def foo(a = 1, b = 2):
    return a + b

# x = foo - 1 ==> TypeError: the function is not being invoked
x = foo() - 1