a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

# This solution preserves the order of the original iterable
from collections import OrderedDict

b = ["1", 1, "1", 2]
b = list(OrderedDict.fromkeys(b))
print(b)

# Explanation 2:

# Ordered dictionaries are another data type in Python that, unlike sets and normal dictionaries they preserve the order of the items. 
# Here OrderedDict.fromkeys(a)  would produce a OrderedDict  like [('1', None), (1, None), (2, None)] . 
# Then we would convert that OrderedDict  to a list.

c = ["1", 1, "1", 2]

d = []

for i in c:
    if i not in d:
        d.append(i)

print(d)


# Explanation 3:

# This is another solution that would preserve the original order. We go through all the original list items and append them to the new list if they have not been appended before. 
# The downside of this is that the operation can take a lot of time if the list as large as we need to access both lists and perform a conditional in each iteration.