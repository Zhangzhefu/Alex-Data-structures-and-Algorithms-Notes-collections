"""
Dynamic Programming

Use Memoization if recursion is natural for the problem but has repeated subproblems.
Use Tabulation if building a table iteratively is easier and avoids recursion overhead.
Dynamic Programming is a powerful tool for solving problems efficiently when brute force is too slow.

A. Overlapping Subproblems
A problem has overlapping subproblems if solving it involves solving the same smaller problem multiple times.
Example: Fibonacci numbers
B. Optimal Substructure
A problem has optimal substructure if the optimal solution to the overall problem can be built from optimal solutions to its subproblems.
Example: Shortest path in a graph.
C. Memoization vs. Tabulation
There are two main ways to implement dynamic programming:

Memoization (Top-Down Approach)

Solve the problem recursively.
Store (cache) results of subproblems in a dictionary or an array.
Reuse previously computed values instead of recomputing them.
Tabulation (Bottom-Up Approach)

Solve the problem iteratively by building a table from smaller subproblems.
Compute solutions in order from smallest to largest.
"""

"""
Observation:

1. Read problem statement
    - Reduce to our own words
    - Read samples

2. Identify key words and phrases
    - Make concrete definition
    - What is possible?
    - What is not possible?
    - Revisit as needed

3. Identify directions of processing
    - Does the problem force us to go in a certain direction?
    If any direction is good, which one is simplest or optimal

4. Main Ideas:
    Statement --> Properties
    Observation is the heart of problem solving.
    Write properties down so we don't have to rediscover them. 
"""

"""
Simulation:

1. Pick an example and work though it
    - Write out the decision/decisions
    - Pick a starting place based on our observations
    - Identify the actions that can be made
    - Identify the consequences of each decisions
    - Simulate enough to gain a structure

2. Replace values with variables
    - Working with values allow us to study 1 example
    - Working with variables allows us to study the entire class of examples.
    
3. Main ideas:
    Properties --> Structure
    Figure out what technique we need to use.
    Working with generalized examples builds structure to abstract ideas
    Instead of guessing the techniques, let the structure and observation reveal itself
    
"""

"""
Recursion:

1. Starting with the recurrence relation
    - Base case?? For what problem?
    - Actions               --> Recursive calls
    - Consequences          --> Transitions
    - Contributions         --> Return Value
    - Affected variables    --> Parameters

2. Obey the rules of recursion:
    1. Base case must be correct
    2. Recursive calls shrink to a basecase
    3. Assume recursive calls are correct

3. Builds base cases from the calls
    - Name the function on it's promise!
    - Avoid simulating/visualizing, it's painful
    - Recursion is naturally inductive 
    - Read aloud and see if it makes sense

4. Main Ideas:
     Structure --> Technique

     Recursion:
        Where: Subtasks have the same shape
        Why: To simplify a problem with induction
        How: Use induction!!

    Don't think more than 1 recurrence down name a function on it promises to do.
    No prints or simulation, just read it aloud.
"""

"""
Dynamic programming:

1. Requirements:
    - Must have recurrence relation
        - Function must be pure: no side effects
    - Recurrence Relation < Recursive execute

2. Time Complexity:
    (# Unique states) * (Cached Complexity)
    # Unique states:
        - Size of recurrence relation
        - Usually the product of parameter bounds
    Cached Complexity:
        - What's the time complexity assuming recursive calls are O(1)

3. DP = Decision Parameterization
    - Decisions are values to compute once
    - Decisions are not tasks to run every time
    - More parameters -> Higher runtime
    - Minimize the parameters needed for a decision
    - Minimize the time to complete the decision
    
4. Main ideas:
    Technique --> More techniques
    Recurrence relation != Recursive execution
    A recurrence relation is a mathematical construct
        - It does not have a side effect
        - It does not "compute" anything
        - It does not require recursive execution
        - It's just a relationship between states
    
    Dynamic Programming:
        - Decomposes problems with recurrence relations
        - Recursive terms are values calculated once
        - Evaluated in a valid order of dependencies  
"""

"""
Fibonacci Sequence:
F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1
"""


# -- Memoization (Top-down)
def fibonacci_memo(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
# This method avoids repeats


print(fibonacci_memo(10))  # Fast!


# -- Tabulation (Bottom-up)
def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(fibonacci_tab(10))  # Fast!


"""
THIS IS FOR LONGEST PALINDROMIC SUBSEQUENCE

# reads forward and backward the same
# We start from both sides, left and right and we meet in the middle. If left and right are the same
# we make them continue going and see if they'll meet in the middle.
# Else, we find the biggest between left and right and move one of them one step to the middle.
# Why "+2"?
# Since s[left] and s[right] are equal, they contribute 2 to the LPS length.
"""


def lps(s, left, right, memo={}):
    if left > right:
        return 0
    if left == right:
        return 1
    if s[left] == s[right]:
        memo[(left, right)] = 2 + lps(s, left+1, right-1, memo)
    else:
        memo[(left, right)] = max(lps(s, left+1, right, memo), lps(s, left, right-1, memo))
    return memo[(left, right)]


"""THIS IS FOR LONGEST PALINDROMIC SUBSTRING"""


def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Substring length
    
    if not s:
        return 0
    
    max_length = 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # Odd-length palindrome
        len2 = expand_around_center(i, i+1)  # Even-length palindrome
        max_length = max(max_length, len1, len2)
    
    return max_length


start = input()
print(longest_palindromic_substring(start))


def lengthOfLIS(self, nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(n):  # Fix the endpoints of subsequence
        for j in range(i):  # Look back at all earlier elements
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1  # Can extend the subsequence ending at j
    return max(dp)  # Gives the LIS length across all endpoints


# Literally go through every possible length, and gives the largest
