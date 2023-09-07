"""
1)print odd value between 20 and 80, without using if. 
Using for loop only.
"""

for i in range (20,80):
    if(i%2!=0):
        print(i)

""""
2) creat a list of 1 to 20 number using 
for loop [1,2,3..20]

"""

a=[]
for i in range (1,21):
    a.append(i)
print(a)


"""
3)create a  list of 20 to 1 value using  for loop 
(dont Use Reverse)
[20,19,18,...3,2,1]

"""

a=[]
for i in range (1,21):
    a.append(i)
print(a[::-1])

"""
 4)take Cube of odd values between 20 to 40
 
 """
for cube in range (20,40):
    if(cube%2!=0):
        print(cube**3," ")

"""
5) take 5 freinds name in list name=[a,b,c,d,e]
take corresponding ages in second list age = [20,21,23,25,24]
expected ans:
    my name is a , my age is 20
    my name is b, my age is 21

"""

name=['s1','s2','s3','s4','s5']
age=[21,22,23,24,25]

for i in range (1,5):
    print(f'My name is {name[i]} and my age is {age[i]}')