'''🔴 Pattern 4 — Cycle Detection
1️⃣ LC 261 — Graph Valid Tree (Concept)
Valid Tree ki 2 conditions:
✅ Cycle nahi honi chahiye
✅ Saare nodes connected hone chahiye
Undirected graph adjacency list

DFS with:

node + parent

Connectivity check:

len(visited) == n
Note: LeetCode par question locked tha, isliye concept cover karke aage badhe.
2️⃣ LC 207 — Course Schedule ✅
Directed graph

Prerequisites ka meaning:

[course, prerequisite]

Graph direction:

prerequisite → course

3-State DFS

0 → Unvisited
1 → Visiting
2 → Completely Processed

Cycle detection:

state[neighbor] == 1 → Cycle
Complete code khud step-by-step likha ✅
🎯 Pattern 4 Status
Undirected DFS Cycle Detection     ✅
Undirected BFS Cycle Detection     ✅
Directed Recursion Stack           ✅
Directed 3-State DFS               ✅
LC 684 — Redundant Connection      ✅
LC 261 — Graph Valid Tree          🔒 Concept Done
LC 207 — Course Schedule           ✅
LC 210 — Course Schedule II        ⏳ Next'''