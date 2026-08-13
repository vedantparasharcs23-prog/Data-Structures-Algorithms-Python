from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)




'''print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)'''

#Traveral Order 

def preOrder(root):
    #base case condition
    if root is None:
        return
    print(root.data , end ="-->")
    preOrder(root.left)
    preOrder(root.right)

preOrder(root)
print()


def inOrder(root):
    if root is None:
        return 
    inOrder(root.left)
    print(root.data , end ="-->")
    inOrder(root.right)

inOrder(root)
print()


def PostOrder(root):
    if root is None:
        return 
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data , end ="-->")

PostOrder(root)
print()


def levelOreder(root):
    if root is None:
        return 
    queue=deque([root])
    while queue:
        node = queue.popleft()
        print(node.data , end ="-->")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

levelOreder(root)
        

#output
'''
10-->20-->40-->50-->30--> PreOrder 
40-->20-->50-->10-->30--> InOrder
40-->50-->20-->30-->10--> PostOrder
10-->20-->30-->40-->50--> LevelOrder
'''

