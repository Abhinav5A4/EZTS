#P1 Panagram hackerrank
#Approach-1 set approach
'''
s=str(input())
s1={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
for ch in s:
    if ch.lower() in s1:
        s1.remove(ch.lower())
if len(s1)==0:
    print("panagram")
else:
    print("not panagram")
'''
'''
#Without using strings
s=int(input())
s1=set(s)
if len(s1)==27:
    print("panagram")
else:
    print("Not a panagram")
'''
#Approach-2 using dictionaries
'''
d=input()
d1={}
d=d.lower()
for i in d:
    if i in d1 or i==" ":
        continue
    d1[i]=1
if len(d1)==26:
    print("Panagram")
else:
    print("Not a panagram")
'''
#P2 Find first repeating character Hackerrank
'''
t=int(input())
for _ in range(t):
    s=input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
for key,val in d.items():
    if val>1:
        print(key,val)
        break
else:
        print('.')
'''
#P3 DICT AND MAP Hackerrank
'''
n=int(input())
d={}
for i in range(n):
    name,no=input().split()
    d[name]=no
while 1:
    x=input()
    if x in d:
        print(x,"=",d[x]) #print(f"{x}={d[x]}")
    else:
        print("Not Found")
'''
#P4
#Approach-1
'''
n=int(input())
d={}
for i in range(n):
    w=input()
    if w in d:
        d[w]+=1
    else:
        d[w]=1
maxval = 1
for val in d.values():
    maxval=max(maxval,val)
l = []
for key,val in d.items():
    if val == maxval:
        l.append(key)
l.sort()
print(l[-1], maxval)
'''
#P5
'''
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    d={}
    for j in range(r):
        sid,cid=map(int,input().split())
        if cid not in d :
            d[cid]=[sid]
        else:
            d[cid].append(sid)
    for j in d:
        if len(d[j])>n:
            print(f"Scenario #{i+1}:Impossible")
            break
        else:
            print(f"Scenario #{i+1}:Possible")
'''
#P6 Graphs store values
'''
n=int(input())
d={}
for i in range(n):
    x,y=input().split()
    if x not in d:
        d[x]=list()
    d[x].append(y)
print(d['a'])
'''
#P7
