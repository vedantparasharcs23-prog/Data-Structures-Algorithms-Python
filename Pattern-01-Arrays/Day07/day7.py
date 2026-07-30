#167
'''arr=[2,7,9,11]

target=9

n=len(arr)
left=0
right=n-1

while left < right:
    CurrentSum=arr[left]+arr[right]

    if CurrentSum > target:
        right-=1
    elif CurrentSum < target:
        left+=1
    else:
        print(left+1,right+1)
        break'''


#remove duplicate
'''nums = [0,0,1,1,1,2,2,3,3,4]
n=len(nums)
left = 0
right = 1

while right <n:
    if nums[left]==nums[right]:
        right+=1
    else :
        left += 1
        nums[left] = nums[right]
        right+=1
print(nums)
print(left+1)'''



#moves zeros

'''arr=[0,1,0,3,13]
n=len(arr)
right=0
for left in range(n):
    if arr[left]!=0:
        arr[left],arr[right]=arr[right],arr[left]
        right+=1
print(arr)'''


#merge sorted  array

'''nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

i=m-1
j=n-1
k=m+n-1


while j>=0:
    if nums1[i]>nums2[j] and i>=0:
        nums1[k]=nums1[i]
        i-=1
        k-=1
    else:
        nums1[k]=nums2[j]
        j-=1
    k-=1
print(nums1)'''


#container with most water
height = [1,8,6,2,5,4,8,3,7]

'''left = 0
right = len(height)-1
maxArea = 0

while left < right:
    width= right-left

    currHeight = min(height[left], height[right])

    area = width * currHeight

    maxArea = max(maxArea, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(maxArea) '''



