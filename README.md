# Classical Computing
Each weeks work understanding code will be posted here.

	Your assignment each week will be to take the diffrent coding language posted above and read through it, and by intuition and what you already know you can write notes on what you think it does, each week in class we'll discuss the piece of code and what it does, be prepared to start the conversation by looking at your notes and asking a question about something in the code that you didn't understand or wanted to know the meaning behind.


# Calc.py This weeks code

```py
# Generally speaking, good developers/programmers write comments like the one you're reading now.
# These comments are useful to get an overview or understand a more complex function.
# In a way your job is to look at this code that I have removed the comments from 
# and your notes will become your own comments on what the program does.




def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

   return x * y

def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
```
