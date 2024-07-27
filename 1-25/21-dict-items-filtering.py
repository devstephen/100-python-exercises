d = {"a": 1, "b": 2, "c": 3}


d = dict((key, value) for key, value in d.items() if value <= 1)

print(d)



k = {"a": 100, "b": 212, "c": 30}

k = dict((key, value) for key, value in k.items() if value > 5)
print(k)


# Explanation: 

# Here we're using a dictionary comprehension. The comprehension is the expression inside dict() . 
# The comprehension iterates through the existing dictionary items, and if an item is less or equal to 1, 
# the item is added to a new dict. 
# This new dict is assigned to the existing variable d  , so we end up with a filtered dictionary in d.