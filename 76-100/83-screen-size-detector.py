from screeninfo import get_monitors 

# Solution 1
for m in get_monitors():
    width = m.width
    height = m.height

print(f"Width: {width}, Height: {height}")


# Solution 2
wide = get_monitors()[0].width
high = get_monitors()[0].height
print(f"Width: {wide}, Height: {high}")

# Explanation:

# We're using the get_monitors  method of the screeninfo  library which can be installed with pip install screeninfo . 
# The get_monitors  method produces a list like [monitor(1920x1080+0+0), monitor(1280x1024+-1280+-31)]  listing all the monitors connected to the computer. Applying [0]  to that list gives the first monitor object out of the list. 
# Applying width  to that monitor, the object gives the width of the monitor, and the same goes for the height  property.