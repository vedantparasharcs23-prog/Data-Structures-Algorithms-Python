'''# Graph Basics

# 1. Graph
# Graph = Nodes (Vertices) + Edges (Connections)

# Example:
# A ----- B
# |       |
# C ----- D
#--------------------------------------------------------------------
# 1 — Empty Matrix

#4 nodes hain, isliye 4 × 4 matrix:

graph = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

Step 2 — Edges add karo

Edges hain:

A-B
A-C
B-D
C-D'''

'''
#Undirected hai, isliye har edge dono directions mein add hogi:

graph[0][1] = 1
graph[1][0] = 1

graph[0][2] = 1
graph[2][0] = 1

graph[1][3] = 1
graph[3][1] = 1

graph[2][3] = 1
graph[3][2] = 1


print(graph) #[[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
for row in graph:
    print(row)
'''

'''
[0, 1, 1, 0]
[1, 0, 0, 1]
[1, 0, 0, 1]
[0, 1, 1, 0]

'''
'''
#Step 1 — Empty dictionary
graph = {
    "A": [],
    "B": [],
    "C": [],
    "D": []
}


#Step 2 — Connections add karo
#Kyuki graph undirected hai, har connection dono nodes mein add hoga:

graph["A"].append("B")
graph["B"].append("A")

graph["A"].append("C")
graph["C"].append("A")

graph["B"].append("D")
graph["D"].append("B")

graph["C"].append("D")
graph["D"].append("C")

for node in graph:
    print(node, "->", graph[node])'''
'''
A -> ['B', 'C']
B -> ['A', 'D']
C -> ['A', 'D']
D -> ['B', 'C']
'''

'''
#Edge List implementation
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D")
]
for edge in edges:
    print(edge)



'''
('A', 'B')
('A', 'C')
('B', 'D')
('C', 'D')
'''

'''

'''
 Small Practice

Apni file mein ye graph banao:

A ---- B
|      |
C ---- D
 \    /
   E

Edges:

A-B
A-C
B-D
C-D
C-E
D-E'''
#print("--------------------------------------------------")
'''EdgesList=[
    ("A","B"),
    ("A","C"),
    ("B","D"),
    ("C","D"),
    ("C","E"),
    ("D","E")
]

for edge in EdgesList:
    print(edge)


print("--------------------------------------------------------------------")
#Ab isi graph ki Adjacency List banate hain

graph = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": []
}

graph["A"].append("B")
graph["B"].append("A")

graph["A"].append("C")
graph["C"].append("A")

graph["C"].append("D")
graph["D"].append("C")

graph["B"].append("D")
graph["D"].append("B")

graph["C"].append("E")
graph["E"].append("C")

graph["D"].append("E")
graph["E"].append("D")

for node in graph:
    print(node, "->", graph[node])

print("--------------------------------------------------------")
'''


'''
1️⃣ Degree

Undirected graph mein:

Degree = node ki adjacency list ki length

Example:'

degree=len(graph["A"])
print(degree)#2


for node in graph:
    print(node, "degree =", len(graph[node]))


graph = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": ["A"]
}

indegree = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

for node in indegree:
    print(node, "in-degree =", indegree[node])


print("Outdegree------------------------------------")
for node in graph:
    outdegree = len(graph[node])
    print(node, "out-degree =", outdegree)'''




#BFS Traversal
from collections import deque
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

def BFS(graph , start):
    queue = deque()
    visited=set()

    queue.append(start)
    visited.add(start)

    while queue:
        node=queue.popleft()
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

BFS(graph,"A")

