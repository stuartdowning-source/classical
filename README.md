# Classical Computing
Each weeks work understanding code will be posted here.

>Your assignment each week will be to take the diffrent coding language posted above and read through it, and by intuition and what you >already know you can write notes on what you think it does, each week in class we'll discuss the piece of code and what it does, be >prepared to start the conversation by looking at your notes and asking a question about something in the code that you didn't understand or wanted to know the meaning behind.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xfnRywBv5VM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# Game.py

```py
import pygame as game

#DeFinitions
game.init()

window = game.display.set_mode((1080,720))

game.display.set_caption("Clasical Freeze")


# x , y , w, h , reserved, speed
player = [540, 360, 50, 50, 0, 5]
enemy = [0, 0, 55, 55, 0, 3]



enemyX = enemy[0]
enemyY = enemy[1]
enemyH = enemy[2]
enemyW = enemy[3]

playerX = player[0]
playerY = player[1]
playerH = player[2]
playerW = player[3]
#Definitions

def movePlr():
	global playerX
	global playerY
	global playerH
	global playerW

	key = game.key.get_pressed()
	if key[game.K_a] and playerX > 25:
		playerX -= player[5]
		player[0] -= player[5]

	if key[game.K_d] and playerX < 1080 - playerW + 25:
		playerX += player[5]
		player[0] += player[5]

	if key[game.K_w] and playerY > 25:
		playerY -= player[5]
		player[1] -= player[5]

	if key[game.K_s] and playerY < 720 - playerH + 25:
		playerY += player[5]
		player[1] += player[5]

def moveEnemy():
	global enemyX
	global enemyY
	global enemyH
	global enemyW

	#UP and to the LEFT
	if enemyX > player[0]:
		if enemyY < player[1]:
			enemy[0] -= enemy[5]
			enemy[1] += enemy[5]
	#UP and to the RIGHT
	if enemyX < player[0]:
		if enemyY < player[1]:
			enemy[0] += enemy[5]
		enemy[1] += enemy[5]
	#DOWN and to the LEFT
	if enemyX > player[0]:
		if enemyY > player[1]:
			enemy[0] -= enemy[5]
			enemy[1] -= enemy[5]
	#DOWN and to the RIGHT
	if enemyX < player[0]:
		if enemyY > player[1]:
			enemy[0] += enemy[5]
			enemy[1] -= enemy[5]

def isCollision(x1,y1,x2,y2,bsize):
    if x1 >= x2 and x1 <= x2 + bsize:
        if y1 >= y2 and y1 <= y2 + bsize:
            return True
    return False

run = True
collide = False
while(run):
	game.time.delay(10)

	for event in game.event.get():
		if event.type == game.QUIT:
			run = False
	if collide:
		run = False
	playerX = player[0]
	playerY = player[1]
	playerH = player[2]
	playerW = player[3]

	enemyX = enemy[0]
	enemyY = enemy[1]
	enemyH = enemy[2]
	enemyW = enemy[3]
	movePlr()
	moveEnemy()

	collide = isCollision(playerX - 25, playerY - 25, enemyX - 27, enemyY - 27, 85)
	window.fill((0,0,0))

	game.draw.rect(window, (0, 255, 0), (playerX - 25, playerY - 25, playerH, playerW))
	game.draw.rect(window, (180, 0, 0), (enemyX, enemyY, enemyH, enemyW))

	game.display.update()
game.quit()

```

# Grade.v2.py
```py
import numpy as np
import matplotlib.pyplot as plt


#This function takes an int and returns a letter grade
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    else:   # grade must be B, C, D or F
        if score >= 80:
            letter = 'B'
        else:  # grade must be C, D or F
            if score >= 70:
                letter = 'C'
            else:    # grade must D or F
                if score >= 60:
                    letter = 'D'
                else:
                    letter = 'F'
    return letter

#These variables are used in our while Loop

GradeList = []

#Loops through the
print("When you are done entering grades, enter to continue.")
while(True):

    studentScore = input("What is the students grade: ")

    if(not studentScore):
        break

    studentScoreInt = int(studentScore)
    GradeList.append(studentScoreInt)

    StudenGrade = letterGrade(studentScoreInt)

    print("The student's grade is: " + StudenGrade)

values = GradeList
#this also overwrites the var(values) which makes what we enter meaning less
#unless we comment out the line below
#Example function to print a normal class bell curve
#Last # is num of students (data points)
#values = np.random.normal(50, 25, 67)


input("Press Enter to generate Graph")
plt.hist(values, 10)
plt.show()
```

# Grade.py
```py
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    else:   # grade must be B, C, D or F
        if score >= 80:
            letter = 'B'
        else:  # grade must be C, D or F
            if score >= 70:
                letter = 'C'
            else:    # grade must D or F
                if score >= 60:
                    letter = 'D'
                else:
                    letter = 'F'
    return letter

studentScore = input()
print("The student's grade is: " + letterGrade(studentScore))
```


# Prime.py 

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
