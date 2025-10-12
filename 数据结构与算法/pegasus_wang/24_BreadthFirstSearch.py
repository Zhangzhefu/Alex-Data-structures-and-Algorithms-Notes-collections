from collections import deque

GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D']
}


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    search_queue = Queue()
    search_queue.push(start)
    searched = set()
    while search_queue:
        curnode = search_queue.pop()
        if curnode not in searched:
            print(curnode)
            searched.add(curnode)
            for node in graph[curnode]:
                search_queue.push(node)


print("BFS: ")
bfs(GRAPH, 'A')

#
# bfs_searched = set()
# def attempt_bfs_recursive(graph, start):
#     if start not in bfs_searched:
#         print(start)
#         bfs_searched.add(start)
#     for node in graph[start]:
#         if node not in bfs_searched:
#             attempt_bfs_recursive(graph, node)
#
#
#
#
# print("bfs: ")
# attempt_bfs_recursive(GRAPH, 'A')

DFS_SEARCHED = set()


def dfs(graph, start):
    if start not in DFS_SEARCHED:
        print(start)
        DFS_SEARCHED.add(start)
    for node in graph[start]:
        if node not in DFS_SEARCHED:
            dfs(graph, node)


print("=======================")
print("DFS: ")
dfs(GRAPH, 'A')
