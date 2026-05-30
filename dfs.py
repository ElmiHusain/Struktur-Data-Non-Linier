# DFS
graph = {
    "A": ["B","C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set() # untuk menyimpan node yang sudah dikunjungi

    if node not in visited:
        print(node, end=" ") # mencetak node yang sedang dikunjungi
        visited.add(node) # menandai node sebagai sudah dikunjungi

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited) # rekursif untuk mengunjungi tetangga node

# jalankan DFS
print("hasil DFS : ")
dfs(graph, "A")