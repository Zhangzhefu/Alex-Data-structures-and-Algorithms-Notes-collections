# A palindrome is when a string is the same forward and backward


class Solution:
    """ This shows how to find the longest palindrome using the expand around center algorithm"""
    def longest_palindrome(self, s: str) -> str:
        def expand(i, j):  # i, j is the center, so we expand from there
            left = i
            right = j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]
        for i in range(len(s)):
            odd = expand(i, i)  # If we're center at i, i - it must be odd
            if odd > ans[1] - ans[0] + 1:  # If odd is bigger than the ones before using the formula
                # The formula for the length of a substring starting
                # at left and ending at right

                dist = odd // 2
                ans = [i - dist, i + dist]

            """
            Because we are centered at i, i, it means length must be odd. 
            If we perform floor division of length by 2,
            we will get the number of characters dist on each side of the palindrome
            Therefore, we can determine that the boundaries of the palindrome are i - dist, i + dist
            """
            even = expand(i, i + 1)  # IF we're at i, i + 1 - it must be even
            if even > ans[1] - ans[0] + 1:
                dist = (even // 2) - 1
                ans = [i - dist, i + 1 + dist]

            """
            If we have a palindrome with length 2, then length / 2 = 1, 
            but there are zero characters on each side of the center.
            We can see that dist is too large by 1. Therefore, we will calculate dist as (length / 2) - 1 instead
            The bounds of the palindrome are i - dist, i + 1 + dist.
            """

        i, j = ans
        return s[i:j + 1]
