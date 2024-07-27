def foo():
    global c
    c = 1
    return c

foo()

print(c)

# Explanation:

# Adding global c  fixes the code. That line makes available name c  in the global namespace. 
# Therefore,  print can access the variable c .