'''#fruit in basket
fruits = [1,2,1]
left=0
maxLen=0
n=len(fruits)
freq={}

for right in range(n):

    fruit = fruits[right]

    if fruit in freq:
        freq[fruit]+=1
    else:
        freq[fruit]=1


    while len(freq)>2:
        outgoing = fruits[left]

        freq[outgoing]-=1
        if freq[outgoing]==0:
            del freq[outgoing]

        left+=1

    maxLen=max(maxLen,right-left+1)
print(maxLen)'''

#longest-substring-without-repeating-characters
#simialr to fruit in basket
'''

s = "abcabcbb"
left=0
n=len(s)
freq={}
maxLen=0

for right in range(n):
    ch=s[right]

    if ch in freq:
        freq[ch]+=1
    else: 
        freq[ch]=1

    while freq[ch]>1:
        outgoing=s[left]
        freq[outgoing]-=1

        if freq[outgoing]==0:
            del freq[outgoing]

        left+=1

    maxLen=max(maxLen,right-left+1)
print(maxLen)'''


'''
#424,longest repeating character similar to 1004
s = "ABAB"
k = 2
left = 0
freq = {}
maxLen = 0
maxFreq = 0
n=len(s)


for right in range(n):
    ch=s[right]

    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

    maxFreq = max(maxFreq, freq[ch])

    while (right - left + 1) - maxFreq > k:
        outgoing=s[left]

        freq[outgoing]-=1

        if freq[outgoing]==0:
            del freq[outgoing]
        left+=1

    maxLen=max(maxLen,right-left+1)
print(maxLen)



LC 643   ✅
LC 2461  ✅
LC 485   ✅
LC 1004  ✅
LC 904   ✅
LC 3     ✅
LC 424   ✅
'''