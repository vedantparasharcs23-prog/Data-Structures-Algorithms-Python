'''🔴 Pattern 4 — Cycle Detection
✅ Undirected Graph Cycle Detection
DFS cycle detection concept
Parent concept

Rule:

visited + parent
DFS mein:
Unvisited neighbor → dfs(neighbor, node)
Visited neighbor aur neighbor != parent → Cycle detected
No-cycle graph dry run
Cycle graph dry run
✅ BFS Cycle Detection

Queue mein:

(node, parent)
visited + parent check
BFS cycle detection pseudocode
🔵 Directed Graph Cycle Detection
Directed graph mein cycle concept
Recursion Stack
visited vs recStack

Rule:

neighbor in recStack → Cycle
DFS complete hone par recStack.remove(node)
Complete algorithm + pseudocode
✅ 3-State DFS
0 → Unvisited
1 → Visiting / Current DFS path
2 → Completely processed

Rules:

state == 0 → DFS
state == 1 → Cycle detected
state == 2 → Ignore
Complete dry run bhi kiya ✅
🟢 LC 684 — Redundant Connection
Question understanding
Redundant edge concept
Edge add karne se pehle path check
DFS path existence approach
visited set
current == target base case
Undirected graph creation
Complete DFS solution'''