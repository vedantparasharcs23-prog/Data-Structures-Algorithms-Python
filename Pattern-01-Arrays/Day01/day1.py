'''Questions:

Print array
Sum of array
Average of array
Largest element
Smallest element
Second largest
Second smallest
Count even numbers
Count odd numbers
Reverse array'''


#1  Print array
'''arr= [12,45,65,4,2,4,5]
#using loops
for i in arr:
    print(i, end =" ")'''


# sum of array

'''arr=[12,45,7,86,5]
sum =0
for i in arr:
    sum+=i

print(sum)#155'''

#Average of array
'''arr=[30,80,20,10,35]
n=len(arr)
total=0
for num in arr:
    total+=num
    avg=total//n

print(avg)'''


#largest element 
'''arr=[30,80,20,10,35]
largest=arr[0]
n=len(arr)
for num in range(1,n):
    if arr[num]>largest:
        largest=arr[num]
print(largest)'''


#smallest element
'''arr=[30,80,20,10,35]
smallest=arr[0]
for num in arr:
    if num < smallest:
        smallest=num
print(smallest)'''


#count even odd

'''arr=[1,2,3,4,5,6,7,8,9,10]
counteven=0
countodd=0
for num in arr:
    if num%2==0:
        counteven+=1

    else:
        countodd+=1

print(counteven)
print(countodd)'''


#count positive and negative and zero

'''arr=[-2,-5,-5,0,0,0,0,0,0,56,38,38]

countzero=0
countPosi=0
countNegi=0

for num in arr:
    if num ==0 :
        countzero+=1

    elif num > 0:
        countPosi+=1
    else:
        countNegi+=1

print(countzero)
print(countPosi)
print(countNegi)'''


#reverse array

'''arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)'''



#linear search

'''arr=[10,20,30,40,50]
key=int(input())
n = len(arr)
for i in range(n):
    if arr[i]==key:
        print("index",i)
        break
if arr[i] !=key:
    print("key value not found")'''


'''arr=[10,20,30,40,50]
found=False
n = len(arr)
key=30
for i in range(n):
    if arr[i]==key:
        found = True
        print("index", i)
        break
if not found :
    print("key not found")'''


#count occurance

'''arr=[2,3,4,5,6,2,3,2,2,2,2,2]
key =2
n=len(arr)
count_Occurrences=0

for i in range(n):
    if arr[i]==key:
        count_Occurrences+=1
    
print(count_Occurrences)'''



#check sorted 

'''arr=[13,45,67,80,90]
n=len(arr)
sorted=True

for i in range(n-1):
    if arr[i]>arr[i+1]:
        sorted=False
        break


if sorted:
    print("array is sorted")
else:
    print("array is not sorted")'''



#copy array

'''arr=[10,20,30]
n=len(arr)
new_arr=[]
for i in arr:
    new_arr.append(i)

print(arr)
print(new_arr)'''


#print alternate element
'''arr=[10,20,30,40,50]
n=len(arr)
for i in range (0,n,2):
    print(arr[i])'''


#reverse array

'''arr=[10,20,30,40,50]

n=len(arr)
for i in range (n-1,-1,-1):
    print(arr[i])'''

#find min max element's index

'''arr=[10,20,30,40,50]
n=len(arr)
max_idx=0

for i in range (1,n):
    if arr[cd ..i]>arr[max_idx]:
        max_idx=i

print(max_idx)


min_idx=0
for i in range(1,n):
    if arr[i]<arr[min_idx]:
        min_idx=i

print(min_idx)'''