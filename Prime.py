#in this example you see a for loop, this is a function that is built into python
#It allows something to be run multiple times until some condition is met
#This is a program that will list prime numbers in a range.



lower = 900
upper = 1000


print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
