
"""
Given a list, write a Python code  to 
swap first and last element of the list.
"""
list=[1,2,3,4,5,6]
a=len(list)
list[0],list[-1] = list[-1] , list[0]
print(list)

"""
write code count lenght of string
"""

a=sorted("sushant")
print(len(a))

"""
Write a Python program to get the sum of a only non-negative integer.
ex, [1,4,-5,-20,10] ans is 15

"""
a=[1,4,-5,-20,10]
b=0
for i in range(len(a)):
    if a[i]>=0:
        b=b+a[i]
print(b)



"""
write code of factorial , ex.ans 6 (3*2*1)

"""
n=int(input("Enter your choice number: "))
a=1
for i in range(1,n+1):
    a=a*i
print(a)



        

