# GRAFH (Implementasi graft)--> jaringan
# BFS sama seperti que(antrian)
# Representasi Adjacency List
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
print("Adjacency list:")
for node in graph:
    print(node, "->", graph[node])
