# GRAPH
# (adalah struktur data jaringan)
# Representasi adjancecy list
graph ={
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
print("Adjacency List : ")
for node in graph:
    print(node,"->", graph[node])
    
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
