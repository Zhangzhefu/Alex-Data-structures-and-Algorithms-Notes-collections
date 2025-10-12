"""
If we encounter a question where we arrive at a place in an iteration, and we have to check
both it's left and right has to meet a condition, we can handle it like this:
The two edge cases we have to consider is the first and the last element
"""

l1 = [1, 0, 0, 0, 1]

for i in range(len(l1)):
    if l1[i] == 0:
        left = (i == 0) or (l1[i-1] == 0)
        right = (i == len(l1) - 1) or (l1[i+1] == 0)

"""Take a look at Leetcode question 605 for a better example"""

"""The main point is to solve edge cases, we can simply do 
    (i==0) or (l1[i-1] == 0) to solve ones on it's left side
    (i == len(l1) - 1) or (l1[i+1] == 0) to solve ones on it's right side

"""
