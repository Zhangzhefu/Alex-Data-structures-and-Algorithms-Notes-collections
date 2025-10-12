# This is how to reverse an array/string without the .reverse()

# return arr[::-1]

p = "sdfweeer"
for i in range(len(p)):
    print(p[i:i])
    print(p[i:i + 2])

"""[i:i] means start and stop from the same index since: [start:stop:step]
by starting and ending at the same index, they'll return an empty list(not an actual list)
doing [i:i + 2] will make it return the current and next element of a list or string
because it start at the current one and go to the next index, 
because start:stop stops at the one before the parameter.
"""

# This is how you shift each character of a string down:

s = "ABCDEF"

a = []
for i in range(len(s)):
    a.append(s[i:] + s[:i])

print(a)

final = []
test = ["hello"]
# final.append(test)
final.append(test[:])
print()
"""
If we append the list like final.append(test) we're giving it a reference
The list final only get the actual values of test if we append the like test[:]
That means to take the actual value, think [:] as what's inside that list.
"""


"""
So if we want to check if the current one is the same as the last one in the list
we can do this:
"""
l1 = [1, 1, 2, 2, 3, 3]
for i in range(len(l1)):
    if i > 0 and l1[i] == l1[i-1]:  # This will deal with the edge-case of i=0
        print("duplicate", i)
