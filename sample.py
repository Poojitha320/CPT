'''write a program to find the area of a rectangle of 2 values , which was associated with a single annotation and
return the values where a=4,b=5,x=2,y=4'''

'''def area(a:float,b:float,x:float,y:float)->float:
    a1=a-x
    a2=b-y
    area=a1*a2
    return area
a=int(input("enter a:"))
b=int(input("enter b:"))
x=int(input("enter x:"))
y=int(input("enter y:"))
print(area(a,b,x,y))'''

#annotations using string
'''from typing import List,Optional
def names(n:List[str],seperator: Optional[str]=' ')->str:
    return seperator.join(n)
print(names(['vijay','Ram','John']))
print(names(['220','CSE'],seperator='-'))'''

#tuple arg keyword functions
#program to find the sum of n user input values by tuple args
#syntax: def user_defined_name(*args):
'''def sumnum(*args):
    return sum(args)
nums=input("enter numbers separated by space:")
numbers=[float(x) for x in nums.split()]
res=sumnum(*numbers)
print(f"Sum:{res}")'''

#sorting numbers
'''def sortnum(*args):
    return sorted(args)
nums=input("enter numbers separated by space:")
numbers=[int(x) for x in nums.split()]
res=sortnum(*numbers)
print(f"Sorted order :{res}")
x=res[::-1]
print("descending order:",x)'''

#keyword arguments--> **kwargs  (string with value using a dictionary)
'''def info(hi, **kwargs):
    print(hi)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
info("Heloooo!!",name='michael',age=22, city="gannavaram", language="english")'''

# 3 marks with different subjects
'''def subs(**kwargs):
    total=sum(kwargs.values())
    print("subject wise marks")
    for subjectvalue in kwargs.items():
        print(f"{key}:{value}")'''

#lambda function
'''types of recursion--> tail,head or linear, tree, direct, indirect, nested , linear'''
#linear or head recursion
'''def hrec(n):
    if n==0:
        return 
    print(n)
    return hrec(n-1)
num=int(input("enter the value:"))
hrec(num)'''

#linear rec factorial
'''def lrec_fact(n):
    if n==1:
        return 1
    return n*lrec_fact(n-1)
num=int(input("enter a number:"))
print("Factorial :",lrec_fact(num))'''

#sum of n numbers
'''def sum_num(n):
    res=0
    if n==1:
        return 1
    for i in range(1,n+1):
        res+=i
    return res
num=int(input("enter a number:"))
print("sum of the numbers is:",sum_num(num))'''

#sum of numbers in a digit
'''def sum_dig(n):
    if n==0:
        return 0
    return (n%10)+sum_dig(n//10)
num=int(input("enter number:"))
print(sum_dig(num))'''

#indirect recursion
'''def one(n):
    if n>0:
        print("one:",n)
        two(n-1)
def two(n):
    if n>0:
        print("two:",n)
        one(n//2)
num=int(input("enter number:"))
print(one(num))'''

'''write a code to check the given number is even or odd using the indeirect rec method with boolean output
input:5
output:5 is even? false'''
#source program
'''def ind_num(n):
   if n==0:
      return True
   return is_odd(n-1)
def is_odd(n):
   if n==0:
      return False
   return ind_num(n-1)
num=int(input("enter number:"))
print(num,"is even?",ind_num(num))'''

#tree recursion
'''def tree(n):
    if n<0:
        return 
    print(n)
    tree(n-1)
    tree(n-2)
tree(3)'''

#nested recursion
def nest(n):
    if n>=10:
        return n-1
    return (nest(nest(n+2)))
print(nest(5))