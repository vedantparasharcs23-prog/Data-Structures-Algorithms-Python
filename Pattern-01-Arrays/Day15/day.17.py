#largest rectangle in histogram 

heights = [2,1,5,6,2,3]

n = len(heights)

stack = []

pse = [-1] * n

for i in range (n):
    while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()

    if stack:
        pse[i] = stack[-1]
    stack.append(i)
print(pse)


stackk = []

nse = [n] * n

for i in range(n - 1, -1, -1):
    while stackk and heights[stackk[-1]] >= heights[i]:
        stackk.pop()
    if stackk:
        nse[i] = stackk[-1]
    stackk.append(i)
print(nse)


max_area = 0

for i in range(n):

    width = nse[i] - pse[i] - 1

    area = heights[i] * width

    max_area=max(max_area,area)

print(max_area)