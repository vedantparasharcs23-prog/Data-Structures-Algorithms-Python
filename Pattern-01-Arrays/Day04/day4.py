'''arr = [4, 2, 7, 1, 5, 3]

n = len(arr)

prefix = [0] * n

prefix[0] = arr[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)

def sumRange(left, right):
    if left == 0:
        return prefix[right]
    else:
        return prefix[right] - prefix[left-1]

print(sumRange(1, 4))
print(sumRange(2, 5))
print(sumRange(0, 3))






'''

#Yehi Pivot Index = Equilibrium Index concept hai.

'''arr=[1,7,3,6,5,6]

totalsum=sum(arr)#28
n=len(arr)
leftsum=0
for i in range(n):
    rightsum=totalsum-leftsum-arr[i]


    if leftsum==rightsum:
        print(i)

    leftsum+=arr[i]
'''
