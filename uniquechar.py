"""
This will take input of and provie the unque char
"""


s=raw_input()
k=int(raw_input())
n=len(s)

for x in range(0, n, k):
    slicedStr = s[x : x+k]
    uni =[]
    for y in slicedStr:
        if y not in uni:
            uni.append(y)
    print ''.join(uni)
	