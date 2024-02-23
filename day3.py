#write a program to print the smallest vowel repeating odd number of times given string
'''s=input()
c=""
for i in s:
    if i in "aeiouAEIOU":
        if s.count(i)%2!=0:
            c+=i
print(min(c))'''

#comparing strings
'''s=input()
s1="codeforces"
c=0
for i in range (len(s)):
    if s[i]!=s1[i]:
        c+=1
print(c)''' #test cases 'coolforces','cazeforcez'

#removing same letters in a two given words
'''s1,s2=map(str,input().split())
s3=""
for i in s2:
    if i not in s1:
            s3+=i
print(s3)'''

'''data structures
srucures'''

'''smart interview
minview'''

#write a program to make encryption and decryption with a key value using functions
'''def encryption(s,k):
    s1=""
    for i in s:
        x=ord(i)+k
        s1+=chr(x)
    print(s1)
def decryption(s,k):
    s1=""
    for i in s:
        x=ord(i)-k
        s1+=chr(x)
    print(s1)
k=int(input("enter key value: "))
s=input("enter string: ")
op=input("select operation: ")
if op == "encrypt":
    encryption(s,k)
elif op == "decrypt":
    decryption(s,k)
else:
    print("inproper operation")'''

#write a program to insert a given number in max number
'''s,d=map(str,input().split())
for i in range(leeen(s)):
    if int(s[i]) <= int(d):
        print(s[:i]=+d+s[i:])
        break
else:
    print(s+d)'''

#write a program to print amstrong numbers in a range using strings and functions
'''def amstrong(n,m):
    for i in range(n,m+1):
        s=str(i)
        sum=0
        for j in s:
            sum+=int(j)**len(s)
            if str(sum)==s:
                print(i)
n,m=int(input()),int(input())
amstrong(n,m)'''

#to print n natural numbers using recursion
'''def printing(n):
    if n < 1:
        return 1
    else:
        print(n)
        printing(n-1)
n=int(input())
printing(n)'''

#to print sum of n natural numbers using recursion
'''def printing(n):
    sum=0
    if n < 1:
        return 1
    else:
        print(n)
        return n+printing(n-1)
n=int(input())
sum=printing(n)
print(sum)'''

#to print the factorial of given number
'''def fact(n):
    if n < 1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))'''

#to check strong number or not using strings and recursion
'''def fact(n):
    if n < 1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum==fact(int(i))
    if sum == x:
        return "strong number"
    else:
        return "not a strong number"
x=int(input())
print(strong(x))'''

#to remove duplicates in a list
'''l=list(map(int,input().split()))
l1=[]
for i in l:
       if i not in l1:
           l1.append(i)
print(l1)'''

#sum of odd numbers in a range
'''n,m=int(input()),int(input())
l=[i for i in range(n,m+1) if i%2!=0]
print(sum(l))'''

#to print the sum of odd composite numbers in a given range
def composite(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        return 1
    else:
        return 0
a,b=int(input()),int(input())
l=[]
for i in range(a,b+1):
    if i%2!=0:
        flag=composite(i)
        if flag==1:
            l.append(i)
print(sum(l))
print(l)






























