"""Back tracking"""
"""
Backtracking is a general algorithm technique where we build a solution step-by-step, 
If we realized that are current path cannot possibly lead to a valid solution:
We backtrack(Undo the last step) 

It's often used for:
    Combinatorics problems (Permutation, combination, subsets)
    Constraint satisfaction problems (Sudoku, N-Queens, word search)
    Pathfinding (Maze solving)
    
The Core idea:
We think of it as exploring a maze
1. Choose a direction to go
2. If we hit a dead end, back up to the previous decision point
3. Try a different route
4. Repeat until a solution is found (Or all options are exhausted)
"""


def backtrack(path, options):
    def end_condition(path):
        pass

    def record_solution(path):
        pass

    def is_valid(choice, path):
        pass
    # The above are just fill-ins to stop the errors, below is the real logic
    if end_condition(path):
        record_solution(path)
        return

    for choice in options:
        if is_valid(choice, path):
            path.append(choice)  # Make a choice
            backtrack(path, options)  # Explore further
            path.pop()  # Undo choice (backtrack)


"""Example for permutations"""


def permutations(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])  # Found a full permutation
            # [:] means to append what's actually inside the list
            # if we don't do that we are giving it a reference
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


"""Example of combination (Leetcode 17)"""


def letterCombinations(self, digits: str) -> list[str]:
    if not digits:
        return []
    num_map = {"2": ("a", "b", "c"),
               "3": ("d", "e", "f"),
               "4": ("g", "h", "i"),
               "5": ("j", "k", "l"),
               "6": ("m", "n", "o"),
               "7": ("p", "q", "r", "s"),
               "8": ("t", "u", "v"),
               "9": ("w", "x", "y", "z")}

    res = []

    def backtrack(index, path):
        """Choose, explore, un-choose"""
        if index == len(digits):  # If it's a full length string
            res.append("".join(path))  # We make them into one string
            return

        for char in num_map[digits[index]]:
            # index of the character in the current digit of the dictionary
            path.append(char)
            backtrack(index + 1, path)
            path.pop()  # After returning it pops the last character
            # After all possible combinations are finished, loops to the second character.

    backtrack(0, [])
    return res


# Finding different subsets of a list:


def subsets(self, nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(sol, index):
        if index == len(nums):
            result.append(sol[:])
            return

        # Don't pick nums[index]
        backtrack(sol, index + 1)

        # Pick nums[index]
        sol.append(nums[index])
        backtrack(sol, index + 1)
        sol.pop()

    backtrack([], 0)
    return result
