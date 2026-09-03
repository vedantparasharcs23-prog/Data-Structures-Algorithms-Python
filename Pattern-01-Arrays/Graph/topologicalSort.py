'''from collections import deque

def topologicalSort(n, edges):

    # Graph
    graph = {i: [] for i in range(n)}

    # Indegree
    indegree = [0] * n

    # Build graph + calculate indegree
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Queue mein indegree 0 nodes
    queue = deque()

    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)

    # Answer
    order = []

    # BFS
    while queue:

        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Cycle check
    if len(order) != n:
        return []

    return order

n = 6

edges = [
    [5, 0],
    [5, 2],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]
#print(topologicalSort(n,edges))
#output --> [4, 5, 0, 2, 3, 1]

#cycle case 


n = 3
edges = [
    [0, 1],
    [1, 2],
    [2, 0]
]
print(topologicalSort(n, edges))
#output --> []'''


#DFS topological sort 

'''def topologicalSortDFS(n, edges):
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)

        visited = set()
        order = []

        def dfs(node):

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            order.append(node)


        for node in range(n):
            if node not in visited:
                 dfs(node)

        return order[::-1]

n = 6

edges = [
    [5, 0],
    [5, 2],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]

print(topologicalSortDFS(n, edges))'''
'''Pattern 5 — Topological Sort
Aaj complete kiya:
✅ Topological Sort kya hai
✅ DAG (Directed Acyclic Graph)
✅ In-degree concept
✅ Kahn's Algorithm — BFS
✅ Indegree 0 → Queue
✅ Neighbor ki indegree decrease
✅ Cycle detection using processed nodes
✅ Kahn's Algorithm VS Code implementation
✅ Cycle test case → []
✅ DFS Topological Sort
✅ DFS completion ke baad order.append(node)
✅ order[::-1]
✅ DFS Topological Sort VS Code implementation
✅ Multiple valid topological orders samjhe
LeetCode connection:
🔁 LC 207 — Course Schedule (revision connection)
🔁 LC 210 — Course Schedule II (revision connection)
▶️ LC 802 — start kiya, kal continue karenge'''