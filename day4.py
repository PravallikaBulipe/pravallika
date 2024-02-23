#to print the sum of even palindromes in a range and also print list of palindromes
'''def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
n,m=int(input()),int(input())
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)
    if flag==1:
        l1.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)
print(l1)
print(sum(l2))'''

#to print sum of the given matrix
'''r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
                                              #print(l)
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)'''

#to print product of inside of the matrix
'''r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
a=1
for i in l:
    print(i)
    for j in i:
        a*=j
print(a)
'''

#print sum of max and min element in tuple matrix
'''r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print(max+min)'''

#average of the matrix
#to print the sum of even palindromes in a range and also print list of palindromes
'''def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
n,m=int(input()),int(input())
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)
    if flag==1:
        l1.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)
print(l1)
print(sum(l2))'''

#to print sum of the given matrix
'''r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
                                              #print(l)
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)'''

#to print product of inside of the matrix
'''r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
a=1
for i in l:
    print(i)
    for j in i:
        a*=j
print(a)
'''

#print sum of max and min element in tuple matrix
'''r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print(max+min)'''

#average matrix
'''r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
    min,max=1000,0
for i in l:
    for j in i:
        sum+=j
print(sum/r*c)'''


#to print the sum of elements in last column of the matrix
'''r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    sum+=i[c-1]
print(sum)'''

#sum of two matrixes
'''r,c=int(input()),int(input())
l1,l2,l3=[],[],[0]*r
for i in range(r):
    l3[i]=[0]*c
for i in range(r):
    l1.append(tuple(map(int,input().split())))
for i in range(r):
    l2:append(tuple(map(int,input().split())))
for i in range(r):
    for j in range(c):
        l3[i][j]=l1[i][j]+l2[i][j]
for i in l3:
    print(i)'''

#union
'''a={1,2,3,4}
b={2,3,5,6}
print(a.union(b))
print(a|b)'''                  

#intersection
'''a={1,2,3,4}
b={2,3,5,6}
print(a.intersection(b))
print(a%b)'''              

#intersection_update
'''a={1,2,3,4}
b={2,3,5,6}
print(a.intersection_update(b))
print(a)'''

#difference
'''a={1,2,3,4}
b={2,3,5,6}
print(a.difference(b))
print(a-b)'''

#difference_update
'''a={1,2,3,4}
b={2,3,5,6}
print(a.difference_update(b))
print(a)'''

#symmetrix_differrence
'''a={1,2,3,4}
b={2,3,5,6}
print(a.symmetrix_difference(b))
print(a^b)'''

#symmetrix_difference_update
'''a={1,2,3,4}
b={2,3,5,6}
print(a.symmetrix_difference_update(b))
print(a)'''

#isdisjoint
'''a={1,2,3,4}
b={2,3,5,6}
print(a.isdisjoint(b))'''

#issubset
'''a={1,2,3,4}
b={2,3,5,6}
print(a.issubset(b))'''

#issuperset
'''a={1,2,3,4}
b={2,3,5,6}
print(a.issuperset(b))'''

#to check the given string is panagram or not
'''import string
s=input()
s=s.lower()
s1=string.ascii_lowercase
if set(s)==set(s1):
    print("panagram")
else:
    print("not a panagram")'''

#to print count of vowels and list of the vowels in each word of a sentence using functions
'''def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i.lower() in "aeiou":
            vc+=1
            s1+=i
    print("vowel count:",vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)'''

#















