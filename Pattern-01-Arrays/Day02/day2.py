#find second largest
arr=[10,20,30,40,60,55]

'''largest = float('-inf')
second_largest = float('-inf')
for num in arr:
    if num > largest:
        second_largest=largest
        largest=num
    elif num> second_largest and num< largest:
        second_largest=num

print(second_largest)'''


'''smallest= float('inf')
second_smallest = float('inf')
for num in arr:
    if num < smallest:
        second_smallest=smallest
        smallest=num
    elif num< second_smallest and num> smallest:
        second_smallest=num

print(second_smallest)'''

#we have to found  largest and smallest in 1 question
'''arr= [10,20,30,40,60,50,80] 
lar=arr[0]
small=arr[0]

for num in arr:
    if num> lar:
        lar=num
    if num< small:
        small=num

print(lar)
print(small)'''



#find max differnce

'''arr = [4, 3, 10, 2, 9, 1, 8]

min_so_far = arr[0]
max_diff = float('-inf')

for current in arr[1:]:
    diff= current-min_so_far

    if diff > max_diff:
        max_diff=diff

    if current < min_so_far:
        min_so_far=current
print(max_diff)'''




#find leader element  with bruteforce
'''arr=[16,17,4,5,3,2]
n=len(arr)
for i in range(n):
    isLeader=True
    for j in range(i+1,n):
        if arr[j]>arr[i]:
            isLeader=False
            break

    if isLeader:
        print(arr[i])'''
#optimized
'''arr = [16, 17, 4, 5, 3, 2]

n = len(arr)

max_right = arr[n-1]

leaders = []

leaders.append(max_right)

for i in range(n-2, -1, -1):

    if arr[i] > max_right:
        leaders.append(arr[i])
        max_right = arr[i]

leaders.reverse()

print(leaders)
'''


#find max and min product
'''arr = [2, 3, -2, 4]

n = len(arr)

max_product = float('-inf')
min_product = float('inf')

for i in range(n):

    for j in range(i,n):

        product = 1

        for k in range(i,j+1):

            product *= arr[k]

        if product > max_product:
            max_product = product

        if product < min_product:
            min_product = product


print(max_product)
print(min_product)

'''

'''arr = [2, 3, -2, 4]

max_product = arr[0]
min_product = arr[0]
answer1 = arr[0]
answer2=arr[0]

for num in arr[1:]:

    temp_max = max(num, 
                   num * max_product, 
                   num * min_product)

    temp_min = min(num, 
                      num * max_product, 
                      num * min_product)

    max_product = temp_max

    min_product = temp_min
    answer1 = max(answer1, max_product)
    answer2 = min(answer2, min_product)
print(answer1)
print(answer2)
'''
#kardanes Algo
'''arr = [-2,1,-3,4,-1,2,1,-5,4]

n = len(arr)

max_sum = float('-inf')

for i in range(n):

    current_sum = 0

    for j in range(i, n):

        current_sum += arr[j]

        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)



arr = [-2,1,-3,4,-1,2,1,-5,4]

current_sum = arr[0]
max_sum = arr[0]

for num in arr[1:]:

    current_sum = max(num, current_sum + num)

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)'''

'''
Pattern 2 – Array Problems
 
✅ LC 121 – Best Time to Buy and Sell Stock
✅ LC 122 – Best Time to Buy and Sell Stock II
✅ LC 53  – Maximum Subarray (Kadane's Algorithm)
✅ LC 152 – Maximum Product Subarray
✅ LC 238 – Product of Array Except Self
✅ LC 283 – Move Zeroes (Two Pointer)
✅ LC 189 – Rotate Array (Reverse Algorithm)
✅ LC 268 – Missing Number (Sum + XOR)
✅ LC 287 – Find Duplicate Number (Floyd Cycle Detection)
'''

