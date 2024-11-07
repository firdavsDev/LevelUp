# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d["b"] = 2
d["d"] = 4
d["a"] = 1
d["c"] = 3

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od["b"] = 2
od["d"] = 4
od["a"] = 1
od["c"] = 3

for key, value in od.items():
    print(key, value)

"""
Deffernce between Dict and Ordered Dict:
1. Dict:
    - A Dictionary in Python is an unordered collection of data values.
    - It stores data in key:value pair.
    - It is a mutable data structure.
    - It is not iterable.
    - It does not maintain the order of the data.
    - It does not allow duplicate keys.
2. Ordered Dict:
    - An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
    - It maintains the order of the data.
    - It is iterable.
    - It allows duplicate keys.
    - It is a mutable data structure
    - It is a subclass of the built-in dict class.

Example:
d = {}
d["b"] = 2
d["c"] = 3
d["a"] = 1
d["d"] = 4

for key, value in d.items():
    print(key, value)

Output:
b 2
c 3
a 1
d 4

od = OrderedDict()
od["b"] = 2
od["d"] = 4
od["a"] = 1
od["c"] = 3

print(od)

Output:
OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
"""
