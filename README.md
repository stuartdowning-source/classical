# Classical Computing
Each weeks work understanding code will be posted here.

>Your assignment each week will be to take the diffrent coding language posted above and read through it, and by intuition and what you >already know you can write notes on what you think it does, each week in class we'll discuss the piece of code and what it does, be >prepared to start the conversation by looking at your notes and asking a question about something in the code that you didn't understand or wanted to know the meaning behind.

<iframe width="560" height="315" src="https://www.youtube.com/embed/u-OmVr_fT4s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Prime.py This weeks code

```py
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
```
