'''stack=[]

stack.append(10)
stack.append(20)
stack.append(30)

x=stack.pop()
stack.append(40)
print(x)
print(stack)'''


#valid_parentheses
'''s = "()[]{}"

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

stack = []

valid = True

for ch in s:

    # Opening bracket
    if ch in "([{":
        stack.append(ch)

    # Closing bracket
    else:

        # Stack empty
        if not stack:
            valid = False
            break

        # Matching check
        if stack[-1] != pairs[ch]:
            valid = False
            break

        # Match found
        stack.pop()

if valid and not stack:
    print(True)
else:
    print(False)'''

#remove all adjacent duplicate in string
'''s = "abbaca"
stack=[]
for ch in s:
    if len(stack)==0:
        stack.append(ch)

    elif stack[-1]==ch:
        stack.pop()
    else:
        stack.append(ch)

ans="".join(stack)
print(ans)'''


#baseball Game

'''ops = ["5","2","C","D","+"]
stack=[]

for op in ops:
    if op not in "CD+":
        stack.append(int(op))

    elif op=='C':
        stack.pop()

    elif op=='D':
        stack.append(stack[-1]*2)
    else:
        stack.append(stack[-1]+stack[-2])
print(sum(stack))
print(stack)'''


#Backspace String Compare

'''s = "ab#c"
t = "ad#c"

stack1 = []
stack2=[]

for ch in s:
    if ch != "#":
        stack1.append(ch)

    else:
        if stack1:
            stack1.pop()

for ch in t:
    if ch != "#":
        stack2.append(ch)

    else:
        if stack2:
            stack2.pop()

print(stack1 == stack2)'''


#Min Stack
'''stack = []
minStack = []

def push(x):
    stack.append(x)

    if not minStack:
        minStack.append(x)

    else :
        minStack.append(min(x,minStack[-1]))
def pop():
    stack.pop()
    minStack.pop()
def top():
    return stack[-1],minStack[-1]

def getMin():
    return minStack[-1]


push(7)
push(3)
push(5)
push(2)
push(6)

print(stack)
print(minStack)



print(getMin())

pop()

print(stack)
print(minStack)

print(getMin())

print(top())'''

#problems/implement-queue-using-stack
'''inputStack=[]
outputStack=[]


def push(x):
    inputStack.append(x)'''


'''push(1)
push(2)
push(3)

print(inputStack)#[1, 2, 3]

print(outputStack)#[]

'''
#-------------------------------------------------------------------------------------------------------
inputStack = []
outputStack = []


def push(x):
    inputStack.append(x)


def pop():
    if not outputStack:
        while inputStack:
            outputStack.append(inputStack.pop())

    return outputStack.pop()


def peek():
    if not outputStack:
        while inputStack:
            outputStack.append(inputStack.pop())

    return outputStack[-1]


def empty():
    return not inputStack and not outputStack


# ---------------- TEST ----------------

push(1)
push(2)
push(3)

print("Input Stack :", inputStack)
print("Output Stack:", outputStack)

print("Peek :", peek())      # 1

print("Pop  :", pop())       # 1
print("Pop  :", pop())       # 2

push(4)

print("Peek :", peek())      # 3

print("Pop  :", pop())       # 3
print("Pop  :", pop())       # 4

print("Empty :", empty())    # True