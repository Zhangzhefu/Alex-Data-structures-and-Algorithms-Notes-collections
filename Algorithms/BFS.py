
"""BFS explores all the neighbors of a node before moving to the next level. It spreads out level-by-level
(useful for shortest paths, level-order traversals, etc.)."""

"""
Breadth first search on the other hand always expands and explores the shallowest nodes first
This is why when implementing a breadth-first search algorithm we use queue (first-in first-out)

Meaning we are exploring nodes by how early you get to the frontier. 

Breadth first search doesn't work the same as Depth-first search in the context of depth.
BFS doesn't pick on path and go to the end, BFS instead kinda explores multiple path at once,
it keep checking which path is closer to the initial state, and explores that one.

This will cause it to for example, take a step in the left path, then the right path, then left, then right...
This is why breadth first search is usually faster and maze solving.

BFS choose the path that's closer to the start, explores it a by one step
then checks again to see who's closer to the start.

"""

from collections import deque


def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)

        # Process the node here

        for neighbor in node.neighbors:
            queue.append(neighbor)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


def levelOrder(root):
    """level order traversal"""
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        result.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result


def levelOrderByLevel(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            # Add children for the *next* level
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)  # Add the finished level to the result

    return result


root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')

print(levelOrder(root))
print(levelOrderByLevel(root))
# Output: [['A'], ['B', 'C'], ['D', 'E', 'F']]


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
