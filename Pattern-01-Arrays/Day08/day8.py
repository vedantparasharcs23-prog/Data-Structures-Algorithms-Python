# 7 Pattern Binary Search
'''nums = [-1,0,3,5,9,12]
target = 10
found=False
left=0
right=len(nums)-1

while left<= right :
    mid = (left+right)//2

    if nums[mid]==target:
        print(mid)
        found=True
        break

    elif nums[mid]< target:
        left=mid+1
    else:
        right=mid-1

if not found:
    print("target not found")'''

# find first and  last occurrance 
'''nums = [1,2,2,2,3,4]
target = 2

left = 0
right = len(nums)-1

ans = -1

while left <= right:
    mid=(left+right)//2

    if nums[mid]==target:
        
        ans=mid
        #first occurrance#right=mid -1
        #last occurrance #left=mid+1

    elif nums[mid]< target:
        left=mid+1
    else:
        right=mid-1

print(ans)'''

#34
'''class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def firstOcc(nums,target):
            left=0
            n=len(nums)
            right=n-1
            ans=-1

            while left<=right:
                mid=(left+right)//2

                if nums[mid]==target:
                    ans=mid
                    right=mid-1

                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return ans
        
        def lastOcc(nums,target):
            left=0
            n=len(nums)
            right=n-1
            ans=-1

            while left<=right:
                mid=(left+right)//2

                if nums[mid]==target:
                    ans=mid
                    left=mid+1

                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return ans
        


        first = firstOcc(nums, target)
        last = lastOcc(nums, target)

        return [first, last]'''


'''nums = [1,3,5,6]
target = 5

left = 0
right = len(nums) - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        print(mid)
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1
else:
    print(left)
'''

#peak element
'''nums = [1,2,3,1]

left = 0
right = len(nums) - 1

while left < right:

    mid = (left + right) // 2

    if nums[mid] < nums[mid + 1]:
        left = mid + 1

    else:
        right = mid

print(left)'''

#search in rotated sorted array
nums = [4,5,6,7,0,1,2]
target = 0
n=len(nums)
left=0
right=n-1

while left<=right:
    mid=(left+right)//2

    if nums[mid]==target:
        print(mid)
        break


    if nums[left]<=nums[mid]:
        #left sorted
        if nums[left]<=target<nums[mid]:
            right=mid-1

        else:
            left=mid+1

    else:
        if nums[mid]<target<=nums[right]:
            left=mid+1
        else:
            right=mid-1
