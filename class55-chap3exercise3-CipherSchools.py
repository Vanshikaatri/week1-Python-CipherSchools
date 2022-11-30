# ques:   exercise one of three
#1. sum of n natural numbers 
#2.  ask a user for natural numbers (n)
#3.  print total from 1 to n 

#ans 
#1. 
n = int(input("enter a number : "))
total = 0
i = 1
while i <=n:
    total +=i
    i+=1
print(total)    