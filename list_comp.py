'''syntax of list comprehensions:
    [expression for var in range() if condition]'''

#program to print squares of numbers --> 1 4 9 16.....100
'''print([num**2 for num in range(1,11)])'''

#list comprehension with condition
'''print([x for x in range(1,11) if x%2==0])'''

#converting into uppercase
'''words=['apple','mango','lytchee']
print([word.upper() for word in words])'''

#step by step list comprhension
'''nums=[int(input(f"enter a number {i+1}:")) for i in range(10)]
print(nums)'''

'''n=[int(x) for x in input("enter 5 nums with space ").split()[:5]]
print(n)'''

#nested list comprehensions +++
'''n=int(input("enter the size of it"))
table=[[i*j for j in range(1,n+1) ] for i in range (1,n+1)]
print("tables of math")
for row in table:
    print (row)'''

#create a nXn matric with manual input numbers only input separated spaces print all the rows in LC only
'''nums=input("enter 9 numbers with space:").split()
if len(nums)!=9:
    print("enter exactly 9 numbers")
else:
    numbers=[int(x)for x in nums]
    matrix=[[numbers[i*3+j]for j in range(3)]for i in range(3)]

for r in matrix:
    print(r)'''

# transpose of a matrix
'''nums=input("enter 9 numbers with space:").split()
if len(nums)!=9:
    print("enter exactly 9 numbers")
else:
    numbers=[int(x)for x in nums]
    matrix=[[numbers[i*3+j]for j in range(3)]for i in range(3)]
    transpose=[[matrix[i][j]for i in range(3)]for j in range(3)]
for r in matrix:
    print(r)
for t in transpose:
    print(t)'''

#flatten a matrix 
'''n=int(input("enter size for nXn:"))
num=[int(x)for x in input("enter numbers").split()[:n*n]]
matrix=[[num[i*n+j] for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)
flat=[k for r in matrix for k in r]
print(flat)'''


#code to consider a list coomprehension: to calculate square of 16 values as nXn matrix and print the list of squares in each row:
'''n=int(input("enter size for nXn:"))
num=[int(x)for x in input("enter numbers").split()[:n*n]]
matrix=[[num[i*n+j]**2 for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)'''

#make the even positions zero
'''n=int(input("enter size for nXn:"))
num=[int(x)for x in input("enter numbers").split()[:n*n]]
matrix=[[num[i*n+j] if num[i*n+j]%2==0 else 0 for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)

#make the odd positions zero
n=int(input("enter size for nXn:"))
num=[int(x)for x in input("enter numbers").split()[:n*n]]
matrix=[[num[i*n+j] if num[i*n+j]%2!=0 else 0 for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)'''

#make the even numbers zero and odd numbers one
n=int(input("enter size for nXn:"))
num=[int(x)for x in input("enter numbers").split()[:n*n]]
matrix=[[0 if num[i*n+j]%2==0 else 1 for j in range(n)]for i in range(n)]
for k in matrix:
    print(k)