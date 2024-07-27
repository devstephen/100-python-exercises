# Challenge 


# def foo(a, b):
#     print(a + b)
 
# x = foo(2, 3) * 10



# Answer: 
def foo(a, b):
    # print(a + b)
    return a + b

a = foo(2,2) * 10

print(a)




# Line 4 throws a TypeError because Python cannot multiply a None type object with an integer. 
# The function output is what produces a None object because the function definition is not returning anything. 
# Fix it by using return  instead of print :