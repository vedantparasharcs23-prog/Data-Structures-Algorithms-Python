'''📚 Pattern 8 — Stack
🔹 Basics
Stack Introduction
LIFO (Last In First Out)
Push
Pop
Peek / Top
Is Empty
Size
Stack using Python List
🔹 Easy Questions
✅ LC 20 — Valid Parentheses
✅ LC 1047 — Remove All Adjacent Duplicates in String
✅ LC 682 — Baseball Game
✅ LC 844 — Backspace String Compare
✅ LC 155 — Min Stack
🔹 Monotonic Stack (Most Important)
🔥 LC 496 — Next Greater Element I
🔥 LC 503 — Next Greater Element II
🔥 LC 739 — Daily Temperatures
🔥 LC 901 — Online Stock Span
🔹 Advanced Stack
🔥 LC 71 — Simplify Path
🔥 LC 150 — Evaluate Reverse Polish Notation
🔹 Hard / Interview Classics
🔥 LC 84 — Largest Rectangle in Histogram
🔥 LC 85 — Maximal Rectangle


'''


'''
Har question ke liye:

Problem samjhenge
Brute force sochenge
Optimal approach nikalenge
Dry run line-by-line
VS Code implementation
LeetCode submit
GitHub push
'''

'''
3-Day Plan
📅 Day 1 as day9
Stack Basics
LC 20
LC 1047
LC 682
LC 844
LC 155
📅 Day 2 as day10
LC 496
LC 503
LC 739
LC 901
📅 Day 3 as day 11
LC 71
LC 150
LC 84
LC 85
'''


#next greater element
'''nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

stack = []
nextGreater = {}

# Step 1: Build Next Greater Dictionary
for num in nums2:

    while stack and num > stack[-1]:
        top = stack.pop()
        nextGreater[top] = num

    stack.append(num)

# Step 2: Remaining elements
while stack:
    top = stack.pop()
    nextGreater[top] = -1

print(nextGreater)

# Step 3: Build Answer
ans = []

for num in nums1:
    ans.append(nextGreater[num])

print(ans)
'''