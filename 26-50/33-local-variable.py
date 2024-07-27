c = 1 # Global variable

def foo():
    c = 2 # Local variable

    return c

c = 3 # Global variable

print(foo())