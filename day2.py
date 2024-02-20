#pizzas 
'''a,b=map(int,input().split(" "))
ns=a*b
if ns%4==0:
    np=ns//4
else:
    np=(ns//4)+1
print(np)'''

'''import math
n,x=map(int,input().split(" "))
ns=n*x
np=math.ceil(c/4)
print(np)'''

#sugarcane
'''x=int(input())
c=x*50
print(c*30/100)'''

#write a python program to print a number which are not divisible by 6,7,8 in a given range
'''n,m=int(input()),int(input())
for i in range (n,m+1):
if i%6!=0 and i%7!=0 and i%8!=0:
    print(i)'''

#write a python program to check given number is prime number or not
'''n=int(input())
for i in range (1,n+1):
    if n%i==0:
     print(i)'''
    
'''n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c == 1:
    print("prime")
else:
    print("not a prime")'''

#to check whether given number perfect or not
'''n=int(input())
sum=0
for i in range (1,n):
    if n%i==0:
        sum+=1
if sum == n:
    print("perfect number")
else:
    print("not a perfect number")'''

#write reverse a number using while loop
'''n=int(input())
rev=0
while n > 0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)'''

'''n=int(input())
rev=0
for i in range (n):
    if n > 0:
        digit=n%10
        rev=rev*10+digit
        n//=10
        break
    else:
        break
print(rev)'''

#write a program to check whether the given number armstrong number or not
'''n=int(input())
temp=n
rev=0
for i in range (n):
    if n > 0:
        digit=n%10
        rev=rev+digit**3
        n//=10
if rev == temp:
    print("amstrong")
else:
    print("not a armstrong")'''


'''n=int(input())
digit=n
rev=0
while n  > 0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev == digit:
    print("amstrong")
else:
    print("not a armstrong")'''

#to print amstrong number in a range using functions
'''def amstrong(n,m):
    for i in range(n,m+1):           #100-1001
        sum=0
        x=i
        while i > 0:
            temp=i%10
            sum+=temp**3
            i//=10
            if sum == x:             #1==100
                print(x)
n,m=int(input()),int(input())        #100-1000
amstrong(n,m)'''

#write a program to print a prime numbers in a range using functions
'''def prime(n,m):
    for i in range(n,m+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
                if c == 2:
                    print(i)
n,m=int(input()),int(input())
primeinrange(n,m)'''

#write a program to check whether the given number is strong number or not using functions
'''def strong(n):
    x,sum=n,0
    while n > 0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum == x:
        return "strong number"          #print("strong")
    else:
        return "not a strong number"    #print("not a strong")
n=int(input())
print(strong(n))                        #strong(n)'''

#strong number in a range
'''def stronginrange(n,m):
    for i in range(n,m+1):
        x,sum=i,0
        while i > 0:
            digit=i%10
            fact=1
            for j in range(1,digit+1):
                fact*=j
            sum+=fact
            i//=10
            if sum == x:
                print(x)
n,m=int(input()),int(input())
stronginrange(n,m)'''

#write a program to remove duplicates in a given string
'''s=input()
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)'''

#write a program to remove conjugative duplicates in a given string
'''s=input()
s1=s[0]
for i in range(1,len(s)):
    if s[i-1]!=s[i]:
        s1+=s[i]
print(s1)'''

#write a program to print count of vowels in both even and odd position
s=input()
s1=""
for in in range(len(s)):
    if i%2==0:
        if s[i] in "aeiouAEIOU":
        














































        

    
        













