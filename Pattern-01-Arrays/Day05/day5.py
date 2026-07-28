'''#sliding window 
arr=[2,1,5,1,3,2]
k=3
n=len(arr)
maxSum=0
windowsum=0

for i in range (k):
    windowsum+=arr[i]

maxSum=windowsum

for i in range(k,n):
    windowsum=windowsum -  arr[i-k] + arr[i]

    maxSum=max(maxSum,windowsum)

print(maxSum/k)'''


#sliding window and hashmap combination
'''
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3

n=len(nums)
windowSum=0
freq={}

for i in range(k):
    windowSum+=nums[i]

    if nums[i] in freq :
        freq[nums[i]]+=1

    else:
        freq[nums[i]]=1
maxSum=0

if len(freq) == k:
        maxSum = windowSum
    

for i in range(k,n):
    outgoing=nums[i-k]
    freq[outgoing]-=1
    if freq[outgoing]==0:
        del freq[outgoing]

    incoming=nums[i]

    if incoming in freq:
        freq[incoming]+=1
    else:
        freq[incoming]=1


    windowSum=windowSum-outgoing+incoming
    if len(freq)==k:
        maxSum=max(windowSum,maxSum)

print(maxSum)'''



'''
✅ Sliding Window concept
✅ Fixed Window
✅ Maximum Sum Subarray
✅ Maximum Average Subarray (LC 643)
✅ Sliding Window + Frequency Map
✅ LeetCode 2461 (Medium)
✅ Dry run khud samjha
'''


#Maximum Consecutive Ones

'''arr=[1,1,0,1,1,1]
count=0
maxCount=0

for num in arr:
    if num==1:
        count+=1
    else:
        count=0
    maxCount=max(maxCount,count)
print(maxCount)
'''

'''
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


left = 0
zeroCount = 0
maxLen = 0
for right in range(len(nums)):
    if nums[right]==0:
        zeroCount+=1

    while zeroCount>k:
        if nums[left]==0:

            zeroCount-=1
        left+=1

    maxLen=max(maxLen,right-left+1)

print(maxLen)'''



'''
Fixed Sliding Window revise ki
LC 643  – Maximum Average Subarray I
LC 2461 – Maximum Sum of Distinct Subarray
LC 485  – Max Consecutive Ones
Variable Sliding Window ka core template samjha
LC 1004 ka VS Code implementation aur LeetCode conversion
'''