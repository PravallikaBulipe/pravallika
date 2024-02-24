#write a program to take dictionary as a input and print keys and values
'''n=int(input("enter a no of items: "))
d={}
for i in range(n):
    key=input("keys: ")
    value=input("value: ")
    d[key]=value
for i in d:
    print("key:",i," ","value: ",{d[i]})
for i in d.keys():
    print(i)
for i in d.values():
    print(i)'''

#your phone book in dictionary
'''n=int(input())
d={}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
m=int(input("No of serch items: "))
for i in range(m):
    s=input()
    if s in d:
        print(s,d[s])
    else:
        print("Not Found")'''

#radiostation
'''d={}
n,m=map(int,input().split())
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
for i in range(m):
    k1,v1=map(str,input().split())
    for i in d:
        if d[i]==v1[:-1]:
            print(f"{k1} {v1} #{i}")'''

#to check the given string is anagram or not
'''s1=input()
s2=input()
if len(s1)==len(s2):
    if sorted(list(s1))==sorted(list(s2)):
        print("true")
    else:
        print("false")
else:
    print("false")'''

#anagram or not using dictionary
'''d={}
for i in range(2):
    k,v=map(str,input().split())
    d[k]=v
print(d)
l=list(d.values())
if len(1[0])==len(1[1]):
    if sorted(list(1[0]))==sorted(list(1[1])):
        print(true)
    else:
        print(false)
else:
    print(false)'''

#program
'''l,d=map(int,input().split())
lst=list(map(int,input().split()))
flag=0
for i in lst:
    for j in lst:
        if i-j==d:
            flag=1
x=True if flag==1 else False
print(x)'''

#find first repeating character
'''s=input()
for i in s:
    if s.count(i)>1:
        print(i)
        break
else:
    print('.')'''

#to print given numbers are prime or composite
'''def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return"composite"
    else:
        return"prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=isprime(i+1)
    d[k]=v
print(d)'''

#write a program t0 maintain students marks database using nested dictionary
'''n=int(input("enter no of students: "))
m=int(input("enter no of subjects: "))
d={}
for i in range(n):
    k=input("enter rollno: ")
    v={}
    for j in range(m):
        sub=input("enter subject name: ")
        marks=int(input("enter marks: "))
        v[sub]=marks
    d[k]=v
for i in d:
    print(i,"=",d[i])'''

#to print average of each students marks using nested dict
'''n=int(input("enter no of students: "))
m=int(input("enter no of subject: "))
d={}
for i in range(n):
    k=input("enter rollno: ")
    v={}
    for j in range(m):
        sub=input("enter subject name: ")
        marks=int(input("enter marks: "))
        v[sub]=marks
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f"{i} : {sum(1)/m}")'''

#implementation of class and object using oops
'''class student:
    def __init__(self,name,age,sec):
        self.name=name
        self.age=age
        self.sec=sec
        print(name,age,sec)
obj=student("pravali","19","b")
obj1=student("lahari","19","b")
obj2=student("geethu","20","b")'''

#implementation of class and object using funtions
'''class ece:
    def section1(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print(name,rollno)
    def section2(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print(self,name,rollno)
obj=ece()
obj.section1("pravali","143")
obj.section2("pravallika","472")'''

'''class training:
    def __init__(self,lang):
        self.lang=lang
    def section1(self):
        print("training section1:",self.lang)
    def section2(self):
        print("tarining section2:",self.lang)
obj=training("python")
obj.section1()
obj.section2()'''

'''class college:
    def __init__(self,name):
        self.name=name
        self.ece1()
        self.ece2()
    def ece1(self):
        print("this is ece-1",self.name)
    def ece2(self):
        print("thisv is ece-2",self.name)
s=input()
obj=college(s)'''

'''class college:
    def __init__(self):
        print(self.sec1())
        print(self.sec2())
    def sec1(self):
        return "method 1"
    def sec2(self):
        return "method 2"
obj=college()'''




























