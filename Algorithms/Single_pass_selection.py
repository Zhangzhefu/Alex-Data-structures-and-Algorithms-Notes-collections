"""
A single-pass selection algorithm is a strategy where:

You iterate through the data only once (hence "single-pass"),

While selecting or identifying specific elements (like max, min, top-k, etc.),

Using constant or limited extra memory (usually O(1) or O(k) for top-k).

"""

"""
| Feature                | Description                                                                  |
| ---------------------- | ---------------------------------------------------------------------------- |
| **Time Complexity**    | O(n), because it goes through the list once                                  |
| **Space Complexity**   | O(1) or O(k), where `k` is number of top elements being tracked              |
| **Streaming-friendly** | Can operate on a stream of values without knowing the whole input in advance |
| **Memory-efficient**   | No sorting or full data structures like heaps unless needed                  |
"""

# generalized code
"""
top_k = [ -∞ ] * k

for num in nums:
    if num in top_k: continue  # Skip duplicates

    for i in range(k):
        if num > top_k[i]:
            # Shift everything right
            top_k[i+1:k] = top_k[i:k-1]
            top_k[i] = num
            break
"""

"""
Use this strategy when:

You're constrained to O(n) time.

Input is too large to sort or hold fully in memory.

You care about extremes (max, min, top-k, etc).

You’re processing a data stream or a large file line-by-line.

=========

Doesn’t work well when:

You need full ordering (sorting required).

You want percentile calculations or averages over complex criteria.

"""

from typing import List


def top_k_distinct_max(nums: List[int], k: int) -> List[int]:
    # Initialize top-k list with -inf
    top_k = [float('-inf')] * k

    for num in nums:
        # Skip if already in top_k to ensure distinct values
        if num in top_k:
            continue

        # Try to insert into the correct position
        for i in range(k):
            if num > top_k[i]:
                # Shift right the smaller elements (going down)
                for j in range(k - 1, i, -1):
                    top_k[j] = top_k[j - 1]
                top_k[i] = num
                break

    # Filter out placeholders (still -inf if not enough distinct values)
    return [x for x in top_k if x != float('-inf')]
