"""
📝If-else

1) grade code
p=50
O: p>75
A : 60 < p>75
B: 50<p<60
C: 35<p<50
fail:p<35

"""
a=int(input("Enter your percentage : "))
if(a>75):
    print("Your grade is O ")
elif(a<=75 and a>=60):
    print("Your grade is A ")
elif(a<=60 and a>=50):
    print("Your grade is B ")
elif(a<=50 and a>=35):
    print("Your grade is C ")
else:
    print("Your are fail")



"""
2) n divisible by 2 or 3
n=7
2 divisble, 3 not
divisible by 2,and 3
divisible by 3, not 2
not divisible by 2, and 3
"""

n=7
if(n%2 | n%3):
   print("YES")