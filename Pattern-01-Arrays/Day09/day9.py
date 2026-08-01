'''stack=[]

stack.append(10)
stack.append(20)
stack.append(30)

x=stack.pop()
stack.append(40)
print(x)
print(stack)'''


#valid_parentheses
s = "()[]{}"

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
    print(False)