# permutations with integers can be delt with using 3 for loops:

digits = [1, 2]
n = len(digits)

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(digits[i]*100 + digits[j]*10 + digits[k])
"""This will print all the 3 digit permutations 
that can be built using the numbers in digits"""


# Substrings
s = "c a t d o g"
n = len(s)
substrings = []
for i in range(n):
    for j in range(i+1, n+1):
        substrings.append(s[i:j])

print(len(substrings))

# Using while loop
sub = []
i = 0
while i < n:
    j = i + 1
    while j <= n:
        sub.append(s[i:j])
        j += 1
    i += 1
print(len(sub))


def permutations(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])  # Found a full permutation
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])

            backtrack(path)  # Explore

            path.pop()  # Undo
            used[i] = False  # Mark unused

    backtrack([])
    return result


print(permutations([1, 2, 3]))
