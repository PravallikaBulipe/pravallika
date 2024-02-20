'''a=10
b=10
print(a is b)
True'''

'''a=10
b=a
print(a is b)
True'''

'''a=10
b=7
print(a is b)
False'''

'''if 3:
    print("hi")'''

    
'''hi
if -45:
    print("hi")'''

#write a python program to print area of circle,recctangle
'''r=int(input("enter radius: "))
l=int(input("enter length: "))
b=int(input("enter breadth: "))
pi=3.14
areac=pi*r*r
arear=1*b
print("area of circle:",areac)
print("area of rectangle:",arear)'''

#greatest of two numbers
'''a=int(input())
b=int(input())
if a > b:
    print(a,"is greater")
else:
    print(b,"is greater")'''

'''a,b=int(input()),int(input())
x="a if greater" if a>b else "b is greater"
print(x)'''

'''print("a if greater" if int(input())>int(input())else "b is greater")'''

#n schoolchildren divide k apples evently,
'''a,b=int(input()),int(input())
print(b%a)'''

#watermelon
'''a=int(input())
n=a/2
if n%2==0:
    print("yes")
else:
    print("no")'''

#atm
'''a,b=map(float,input().split(" "))
if a%5==0:
    if a < b:
            print(b-a)
        else:
            print(b)
else:
    print(b)'''

'''a,b=map(float,input().split(" "))
if a%5==0 and a < b:
            print(b-a)
else:
    print(b)'''

#discount
'''t=100
a=int(input())
x=(a/100)*t
print(100-X)'''

'''t=100
print(100-int(input())/100*t)'''

#discount
'''a,b,c,d=map(int,input().split(" "))
if a-c < b-d:
    print("first")
elif a-c > b-d:
                 print("second")
else:
    print("any")'''

'''a,b,c,d=map(int,input().split(" "))
x=a-a*c/100
y=b-b*d/100
if x < y:
    print("first")
elif x > y:
    print("second")
else:
    print("any")'''

#leapyear or not
'''year=int(input())
if year%4==0 or year%400==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")'''

#candys
'''a,b=map(int,input().split(" "))
if a >= b:
    x=0
else:
    c=a-b
    if c%4==0:
        np=c//4
    else:
            np=(c//4)+1
print(np)'''
    

