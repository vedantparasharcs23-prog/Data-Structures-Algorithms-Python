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


#next greater element in normal array
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

#in circular array 503
'''nums = [1,2,1]

n = len(nums)

stack = []

ans = [-1] * n

for i in range(2 * n):

    current = nums[i % n]

    while stack and current > nums[stack[-1]]:

        idx = stack.pop()

        ans[idx] = current

    if i < n:
        stack.append(i)

print(ans)'''


#daily temperature 

'''temperatures = [73,74,75,71,69,72,76,73]

stack = []

n = len(temperatures)

ans = [0] * n

for i in range(n):

    current = temperatures[i]

    while stack and current > temperatures[stack[-1]]:
        idx = stack.pop()

        ans[idx] = i - idx

    stack.append(i)

print(ans)'''


#simplify Path 71

'''path = "/a/./b/../../c/"

parts = path.split("/")

stack = []

for part in parts:

    if part == "" or part == ".":
        continue
    elif part == "..":
        
        if stack:
            stack.pop()
    else:
        stack.append(part)
    "/" + "/".join(stack)
print("/" + "/".join(stack))'''


#evaluate RPN 150

'''tokens = ["4","13","5","/","+"]

stack = []

for token in tokens:
    if token not in "+-*/":
        stack.append(int(token))
    else:
        right = stack.pop()
        left = stack.pop()

        if token=="+":
            stack.append(left + right)

        elif token=="*":
                    stack.append(left * right)
        if token=="-":
                    stack.append(left - right)
        if token=="/":
                    stack.append(int(left / right))

print(stack[-1])
'''
'''day16
Stack Pattern ✅
Basics
✅ Push
✅ Pop
✅ Peek
✅ Empty
✅ Min Stack
LeetCode
✅ 20 — Valid Parentheses
✅ 1047 — Remove All Adjacent Duplicates
✅ 844 — Backspace String Compare
✅ 682 — Baseball Game
✅ 155 — Min Stack
✅ 496 — Next Greater Element I
✅ 503 — Next Greater Element II
✅ 739 — Daily Temperatures
✅ 71 — Simplify Path
✅ 150 — Evaluate Reverse Polish Notation'''