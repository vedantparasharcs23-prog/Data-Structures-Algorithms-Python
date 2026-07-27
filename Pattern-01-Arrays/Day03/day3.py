'''# count frequency

arr=[1,2,2,3,3,3,4]

freq={}

for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1



for key, value in freq.items():

    if value > 1:

        print(key)
print(freq)'''

# Boyer Moore Voting Algo
'''nums=[2,2,1,1,1,2,2]

candidate=None
count=0

for num in nums:
    if count==0:
        candidate=num
    if num==candidate:
        count+=1
    else:
        
        count-=1
print(candidate)
'''


'''#first repeating element

arr=[4,3,3,4,3,5,6]

freq={}

for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for num in arr:
    if freq[num]>1:
        print(num)
        break'''
#first non repeating element


'''arr=[10,5,3,4,5,3,6] #if arr=[5,3,5,3] return -1
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

for num in arr:
    if freq[num]==1:
        print(num)
        break '''


#Union of two array

arr1=[1,2,3,4,5,]
arr2=[6,7,8,9,10]

ans=set()


for num in arr1:
    ans.add(num)
for num in arr2:
    ans.add(num)
print(list(ans))
