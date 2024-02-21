#P1 Sugarcane juice
'''
def sjb(x):
    return x*15
t = int(input())
for _ in range(t):2
               n=int(input())
               print(sjb(n))
'''
#P1 Approach2
'''
def profit(x):
    x *=0.3
    return int(x*50)
def test(t):
    if t == 0:
        return
    print(profit(int(input())))
    test(t-1)
t = int(input())
test(t)
'''
#P2 watching movie at 2x
'''
def movie(x,y):
    x = x-y//2
    return x
x,y = map(int,input().split())
print(movie(x,y))
'''
#P3 Lucky 4
'''
t = int(input())
for i in range(t):
    c = 0
    n = int(input())
    while (n >0):
        r = n%10
        n = n//10
        if(r == 4):
            c+=1
    print(c)
'''
#P5 X Compute N Hackerrank
'''
import math
n = int(input())
'''
'''
n=int(input())
n=3000+n
print(n*10+3)
'''

def rev(n):
    s=0
    while(n>0):
        r = n%10
        s = s*10+r
        n = n//10
    return s*10+3
n = int(input())
c=print(rev(n))











    
