#user defined function
'''
def hi():
    print("helloooooo")
hi()'''

#user defined functions with arguments
'''def summate(m,n): #m,n are arguments
    print("sum of two numbers:",m+n)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
summate(a,b)'''

#user defined function with args and return values
'''def summate(x,y):
    return x+y
a=int(input("enter a:"))
b=int(input("enter b:"))
print(summate(a,b))'''

#default argument
'''def power(base,exp=3):
    return base**exp
a=int(input("enter base:"))
print(power(a))
print(power(a,2))'''

#multiple return values from a single function
'''def compute(a,b):
    return a+b,a-b,a*b,a//b
a=int(input("enter a:"))
b=int(input("enter b:"))
sum,diff,prod,div=compute(a,b)
print("sum:",sum)
print("difference:",diff)
print("product:",prod)
print("division:",div)'''

#anonumous function like lambda
#lambda var: operation-->syntax
'''num=int(input("enter num:"))
n1=int(input("enter n1:"))
square=lambda num: num**n1
print(square(num))'''

#nested functions
'''def hi():
    def hello():
        print("inner function")
    print("outer function")
    hello()
hi()'''
#nested fun problem
'''def operation(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    print("addition:",add())
    print("subtract:",sub())
a=int(input("enter a:"))
b=int(input("enter b:"))
operation(a,b)'''

#write a program to calculate the factorial and power of the given numbers using nested loop within loop where a=5 and b=3
'''def loop(a,b):
    def fact(a):
        res=1
        for i in range(1,a+1):
            res*=i
        return res
    def power():
        return a**b
    print("factorial of a:",fact(a))
    print("power of a and b:",power())
a=5
b=3
loop(a,b)'''

#recursive factorial problem
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def super_fact(n):
    if n==1:
        return 1
    return fact(n)*super_fact(n-1)
    
num=int(input("enter number:"))
print("factorial:",super_fact(num))