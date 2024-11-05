# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d["b"] = 2
d["c"] = 3
d["a"] = 1
d["d"] = 4

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od["b"] = 2
od["d"] = 4
od["a"] = 1
od["c"] = 3

print(od.pop("a"))
print(od)

# diff between dict and ordered dict
# This is a Dict:

# b 2
