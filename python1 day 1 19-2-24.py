#P1
"""
a = int(input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)
"""
#P2
"""
a,b,c = map(int,input().split())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
            
"""

#P3
"""
a = int(input())
b = int(input())
if a>b:
    print(b)
else:
    print(a)
"""
#P4
"""
a = int(input())
b = int(input())
c = int(input())
if (a>b and a<c) or (a<b and a>c):
    print(a)
elif (b<a and b>c) or (b>a and b<c):
    print(b)
else:
    print(c)
"""
#P4-1 2ND Highest
"""
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    a =0
elif b>a and b>c:
    b =0
else:
    c =0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
"""
#P5
'''
for i in range(1000):
    print("Hello World")
'''
#P6
'''
a,b = map(int,input().split())
if a == b:
    print("a == b")
elif a>b:
    print("a > b")
elif a<b:
    print("a < b")
'''
#P7 triangle or not
'''
a,b,c = map(int,input().split())
if (a < b+c) and (b<a+c) and (c<a+b):
    print("Yes")
else:
    print("No")
'''
#P8 remaining apples
'''
n = int(input())
k = int(input())
while(k>n):
    k = k-n
print(k)
'''
#P9 number reverse
'''
n=int(input())
c=0
if n<0:
    n = -1*n
    c = 1
r=0
x = 0
while(n!=0):
    r =n%10
    x = x*10+r
    n = n//10
if c == 1:
    x = -1*x
print(x)
'''
#P9 Stringmethod
'''
n = int(input())
n = str(n)
n = n[::-1]
print(int(n))
'''
#P10 watermelon divide even
'''
w = int(input())
if(w > 2 and w%2 ==0):
    print("YES")
else:
    print("NO")
'''
#P11 testcase and fever or not
'''
t = int(input())
for i in range(t):
    x = int(input())
    if(x>98):
        print("Yes")
    else:
        print("No")
'''
#P12 SP and Discount 100
'''
t = int(input())
for i in range(t):
    x = int(input())
    print(100-x)
'''
#P13 TV Sale
'''
t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    a = a-c
    b = b-d
    if b>a: #a-c>b-d
        print("First")
    elif b<a:
        print("Second")
    else:
        print("Any")
'''
#P14 Chef and Candies
''' Aproach -1
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if n>x:
        k = n - x
        if k%4==0:
            print(k//4)
        else:
            print((k//4)+1)
    else:
        print(0)
''' 
#P15 Pizzas slices each n friends each x slices
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    ts = n*x
    tp = 0
    while ts>4:
        tp = tp+1
        ts = ts-4
    if tp ==0:
        print(tp)
    else:
        print(tp+1)
        
        

    




