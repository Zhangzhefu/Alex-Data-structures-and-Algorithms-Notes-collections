"""DFS explores as far as possible along each branch before backtracking.
It dives deep into the tree/graph before moving sideways."""

"""After hearing a lecture from a professor teaching about AI, I've figured out some very
important things about Depth first search

Depth-first search works by expanding and exploring the deepest node first.
Essentially, we use a Stack data structure that is last-in first-out.
This means when we're searching, we search the node that is lastly added to the frontier before the other node

Frontier is like the current state we're given to check options and solve our problem

This basically means we're always working with the newest added node. 
New = priority

DFS picks a direction, and explores it to the end, then changes.
"""
"""
DFS can be done in different “flavors,” depending on when you process a node:

    Preorder (Root → Left → Right)
        -- In BST, Useful for save/serializing a tree structure(root is always first)

    Inorder (Left → Root → Right) ← what you used
        -- In BST, using inorder will return a list that is strictly sorted ascending order

    Postorder (Left → Right → Root)
        -- In BST, useful for deleting a tree bottom-up (Process children before parents)
        
They’re all DFS because they recursively explore children before returning up.
"""


def dfs_tree(node):
    if not node:
        return
    print(node.val)          # Preorder step (process current)
    dfs_tree(node.left)           # Go left
    dfs_tree(node.right)          # Go right


def dfs_graph(node, visited, graph):
    if node in visited:
        return
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        dfs_graph(neighbor, visited, graph)


def dfs(node, visited):
    if not node or node in visited:
        return
    visited.add(node)
    # Process the node here (e.g., print(node), sum += node.val, etc.)

    for neighbor in node.neighbors:
        dfs(neighbor, visited)


def dfs_iterative(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            # Process the node here

            for neighbor in reversed(node.neighbors):
                stack.append(neighbor)


"""
Relationships with BSTs:

Inorder traversal is special for BSTs, it always produces a sorted sequence of node values
Preorder/Postorder are more about tree structure, while inorder is about the ordering property

Inorder traversal = sorted values
    This is the defining property of BSTs
    If an inorder is not strictly increasing, the tree is not a valid BST

Preorder + Inorder:
    If we know both preorder and inorder traversals of a BST, we can reconstruct the exact tree

Postorder + Inorder:
    These two can also reconstruct the tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_preorder_inorder(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    index = inorder.index(root_val)
    root.left = build_tree_preorder_inorder(preorder[1:1+index], inorder[:index])
    root.right = build_tree_preorder_inorder(preorder[1+index:], inorder[index+1:])
    return root


def build_tree_postorder_inorder(postorder, inorder):
    if not postorder or not inorder:
        return None

    root_val = postorder[-1]
    root = TreeNode(root_val)
    index = inorder.index(root_val)
    root.left = build_tree_postorder_inorder(postorder[:index], inorder[:index])
    root.right = build_tree_postorder_inorder(postorder[index:-1], inorder[index+1:])
    return root


from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        copied = {}

        def dfs(curr):
            if curr in copied:
                return copied[curr]
            clone = Node(curr.val, [])
            copied[curr] = clone
            for neighbor in curr.neighbors:
                clone_neighbors = dfs(neighbor)
                clone.neighbors.append(clone_neighbors)
            return clone

        return dfs(node)


"""
| Feature / Use Case               | DFS                                           | BFS                                  |
| -------------------------------- | --------------------------------------------- | ------------------------------------ |
| **Data Structure**               | Stack (explicit or recursion)                 | Queue                                |
| **Search Goal**                  | Deep nodes first                              | Shallow nodes first                  |
| **Path Finding**                 | Not optimal for shortest path                 | Best for shortest path (unweighted)  |
| **Cycle Detection (Graph)**      | Yes                                           | Yes                                  |
| **Space Complexity** (tree-like) | O(h), where h = height/depth                  | O(w), where w = width/level          |
| **Use When**                     | Need full exploration, backtracking, or paths | Need shortest path or level-by-level |
"""

"""
| Use Case                           | Recommended Search                       |
| ---------------------------------- | ---------------------------------------- |
| Maze solving / pathfinding         | BFS (shortest path) or DFS (exploration) |
| Topological sort                   | DFS                                      |
| Connected components in a graph    | DFS or BFS                               |
| Tree traversal (inorder, preorder) | DFS                                      |
| Finding shortest path (unweighted) | BFS                                      |
| Solving puzzles (e.g., 8-puzzle)   | BFS (for shortest solution)              |
| Finding cycles                     | DFS                                      |
"""
