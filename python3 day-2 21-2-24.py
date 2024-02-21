#P1 Find duplicate element in array hackerrank
'''
#Approach-1
N = int(input())
L = list(map(int,input().split()))
for i in range(N):
    for j in range(i+1,N):
        if(L[i]==L[j]):
            print(L[i])
'''
'''
#Approach-2
n=int(input())
a=list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break
'''
'''
#Approch-3
n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(n-1):
    if a[i]==a[i+1]:
        print(a[i])
        break
'''
'''
#Approach-4
n=int(input())
a=list(map(int,input().split()))
for i in(a):
    c=a.count(i)
    if c>1:
        print(i)
        break
'''
#P2 Print Non duplicates
'''
#Approach 1
n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(n-1):
    if l[i]!=l[i+1]:
        print(l[i])
'''
#Approach2
n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    if l.count(i)==1:
        print(i,end=" ")

