"""
Prefix sums (also called cumulative sums or running totals) are a fundamental concept in computer science and data
processing where we precompute cumulative totals of elements in a sequence to enable efficient range queries.
The generalized version extends this concept to various operations beyond simple addition.
"""

"""
1. Basic Prefix Sum
For an array nums = [a₀, a₁, ..., aₙ₋₁], the prefix sum array is:
prefix = [0, a₀, a₀+a₁, a₀+a₁+a₂, ..., sum(nums)]
where prefix[i] contains the sum of all elements before index i.

Key Properties:

Construction: O(n) time, O(n) space

Range Sum Query: sum(nums[i..j]) = prefix[j+1] - prefix[i] (O(1) time)
"""

"""
2. Generalized Prefix Sum
This extends the concept to other associative operations (+, ×, ⊕, min, max, etc.):
prefix_op[i] = nums[0] op nums[1] op ... op nums[i-1]


Common Variants:

Multiplicative Prefix Product:
Used for product calculations
Example: [1,2,3,4] → [1, 1×2=2, 1×2×3=6, 1×2×3×4=24]

XOR Prefix Sum:
Useful in bit manipulation problems
Example: [1,2,3] → [1, 1⊕2=3, 1⊕2⊕3=0]

Min/Max Prefix:
Tracks running minimum/maximum
Example (min): [3,1,4,2] → [3, min(3,1)=1, min(1,4)=1, min(1,2)=1]
"""


def build_prefix(nums, op, identity):
    prefix = [identity] * (len(nums)+1)
    for i in range(len(nums)):
        prefix[i+1] = op(prefix[i], nums[i])
    return prefix


"""This also demonstrates exactly how lambda is used"""
# For standard sum
nums = [1, 2, 3]

prefix = build_prefix(nums, lambda a, b: a + b, 0)
print(prefix)

# For product
product_prefix = build_prefix(nums, lambda a, b: a * b, 1)

# For XOR
xor_prefix = build_prefix(nums, lambda a, b: a ^ b, 0)

"""
4. Applications
Range Queries:
Quickly answer "sum/product/XOR between indices i and j"

Equilibrium/Pivot Points:
Like the pivot index problem (LeetCode 724)
Find where left and right portions satisfy some condition

Sliding Window Problems:
Efficiently calculate window properties

Statistical Calculations:
Moving averages, cumulative distributions
"""


# For many problems, you can compute prefix sums on-the-fly without storing the full array:
def pivotIndex(nums):
    """leetcode 724"""
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i
        left_sum += nums[i]
    return -1


"""
Key Insight:
Prefix sums transform O(n) operations into O(1) lookups by paying an O(n) pre-processing cost,
making them invaluable for problems involving frequent range queries or cumulative properties.
"""
