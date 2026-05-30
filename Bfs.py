# BFS
from collections import deque
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
def bfs(graph, start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
           
        for neighbor in graph[node]:
            queue.append(neighbor)

print("Hasil BFS : ")
bfs(graph, "A")
