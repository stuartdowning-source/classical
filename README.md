# Classical Computing
Each weeks work understanding code will be posted here.

>Your assignment each week will be to take the diffrent coding language posted above and read through it, and by intuition and what you >already know you can write notes on what you think it does, each week in class we'll discuss the piece of code and what it does, be >prepared to start the conversation by looking at your notes and asking a question about something in the code that you didn't understand or wanted to know the meaning behind.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PVY46hUp2EM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# Game.py
```py
import pygame as game
import pygame_textinput
import pygame.freetype
import datetime
import math

white = (255,255,255)
yellow = (255, 255, 0)
black = (0,0,0)
var = True
#DeFinitions
class ClassicalFreeze(object):
	def __init__(self, x, y):

		self.x = x
		self.y = y
		game.init()
		self.window = game.display.set_mode((self.x, self.y))
		game.display.set_caption("Clasical Freeze")

		self.frameCount = 0

		self.font = game.freetype.SysFont("Airal.ttf", 24)
		self.time = 0
		self.timestr = "00:00"
		self.run = True
	def quitLoop(self):
		for event in game.event.get():
			if event.type == game.QUIT:
				self.run = False
				return True
			else:
				return False

GameClass = ClassicalFreeze(1080, 720)

class Menu(object):
	def __init__(self, loop):
		GameClass.window.fill(black)
		game.display.update()
		self.i = 1
		self.loop = loop

	def MenuLoop(self):
		for event in game.event.get():
			if event.type == game.QUIT:
				GameClass.run = False

		key = game.key.get_pressed()
		if key[game.K_k]:
			self.loop = False
		if key[game.K_w] and self.i > 0:
			self.i -= 1
		if key[game.K_s] and self.i < 2:
			self.i += 1

		s = 80
		k = 90
		distance = 30

		GameClass.window.fill((0,0,0))
		GameClass.font.render_to(GameClass.window, (1080/2 - 100, 20 + k + distance), "Classical Freeze", white)
		distance += 30

		if self.i == 0:
			GameClass.font.render_to(GameClass.window, (1080/2 - s, 40 + k + distance), "Start", yellow)
		else:
			GameClass.font.render_to(GameClass.window, (1080/2 - s, 40 + k + distance), "Start", white)
		distance += 30
		if self.i == 1:
			GameClass.font.render_to(GameClass.window, (1080/2 - s, 60 + k + distance), "Score Board", yellow)
		else:
			GameClass.font.render_to(GameClass.window, (1080/2 - s, 60 + k + distance), "Score Board", white)
		distance += 30
		if self.i == 2:
			GameClass.font.render_to(GameClass.window, (1080/2 - s, 80 + k + distance), "Quit", yellow)
		else:
			GameClass.font.render_to(GameClass.window, (1080/2 - s, 80 + k + distance), "Quit", white)
		game.display.update()
	def noOp(self):
		return True
	def ScoreBoardLoop(self, score):
		done = False

		#while not done:
			#GameClass.window.fill((255,255,255))
			#events = pygame.event.get()
			#textinput = pygame_textinput.TextInput()
			# Feed it with events every frame
			#if textinput.update(events):
   			#	Done = True
   			# Blit its surface onto the screen
			#GameClass.window.blit(textinput.get_surface(), (10, 10))



		with open("score.txt", 'a', encoding = 'utf-8') as f:
			f.write(GameClass.timestr + "\n")
			f.close()


		GameClass.window.fill((0,0,0))
		file = open("score.txt", "r")
		lines = file.readlines()
		linNum = 60	
		for line in lines:
			linNum += 20
			line = line.rstrip()                                                                                                                                                                                                                         
			GameClass.font.render_to(GameClass.window, (1080/2 - 80, linNum), line, black)
		file.close()

		game.display.update()
		GameClass.quitLoop()
		
		

class powerup(object):
	def __init__(self, x, y, w, h, on):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.on = on

	def Draw(self):
		game.draw.rect(
		GameClass.window,
		(0,0,255),
		(self.x, self.y, self.w, self.h))


class enemy(object):
	def __init__(self, x, y, w, h, r, s):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.r = r
		self.s = s

	def DrawObject(self):
		game.draw.rect(
		GameClass.window,
		(180, 0, 0),
		(self.x, self.y, self.h, self.w))

	def moveEnemy(self, Player):
		#UP and to the LEFT
		if self.x > Player.x:
			self.x -= self.s
		if self.y < Player.y:
			self.y += self.s
		#UP and to the RIGHT
		if self.x < Player.x:
			self.x += self.s
		if self.y < Player.y:
			self.y += self.s
		#DOWN and to the LEFT
		if self.x > Player.x:
			self.x -= self.s
		if self.y > Player.y:
			self.y -= self.s
		#DOWN and to the RIGHT
		if self.x < Player.x:
			self.x += self.s
		if self.y > Player.y:
			self.y -= self.s

class player(object):
	def __init__(self, x, y, w, h, r, s):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.r = r
		self.s = s
	def movePlr(self):
		key = game.key.get_pressed()

		if self.s > 5:
			self.s -= 0.01

		if key[game.K_a] and self.x > 25:
			self.x -= self.s
			#self.x -= self.s

		if key[game.K_d] and self.x < 1080 - self.w + 25:
			self.x += self.s
			#self.x += self.s

		if key[game.K_w] and self.y > 25:
			self.y -= self.s
			#self.y -= self.s

		if key[game.K_s] and self.y < 720 - self.h + 25:
			self.y += self.s
			#self.y += self.s
		#game.time.delay(50)
	def CollideWithObject(self, CollsionObject, bsize):
		if (self.x - 25) >= (CollsionObject.x - 27) and (self.x - 25) <= (CollsionObject.x - 27) + bsize:
			if (self.y - 25) >= (CollsionObject.y - 27)	and (self.y - 25)<= (CollsionObject.y - 27) + bsize:
				return True
			return False

	def DrawObject(self):
		game.draw.rect(
		GameClass.window,
		(0, 255, 0),
		(self.x - 25, self.y - 25, self.h, self.w))



#x
#y
#witdh
#highet
#Reserved (probabably Health)
#speed


#Before game start definitons
plr = player(540, 360, 50, 50, 0, 3)
bad = enemy(0, 0, 55, 55, 0, 1)
power = powerup(45, 35, 10, 10, True)
power2 = powerup(100, 200, 10, 10, True)
power3 = powerup(20, 80, 10, 10, True)
power4 = powerup(30, 100, 10, 10, True)

menu = Menu(True)

while(GameClass.run):
	game.time.delay(10)
	GameClass.frameCount += 1

	GameClass.window.fill((0,0,0))
	GameClass.quitLoop()
	while menu.loop:
		menu.MenuLoop()

	plr.movePlr()
	bad.moveEnemy(plr)

	if (GameClass.frameCount % 100 == 0):
		GameClass.frameCount = 0
		GameClass.time += 1

	GameClass.timestr = str(datetime.timedelta(seconds=GameClass.time))

	if plr.CollideWithObject(bad, 84):
		GameClass.run = False
		while True:
			menu.ScoreBoardLoop(GameClass.timestr)


	if plr.CollideWithObject(power, 10):
		plr.s += 5
		power.on = False
	if plr.CollideWithObject(power2, 10):
		plr.s += 5
		power2.on = False
	if plr.CollideWithObject(power3, 10):
		plr.s += 5
		power3.on = False
	if plr.CollideWithObject(power4, 10):
		plr.s += 5
		power4.on = False

	if power.on:
		power.Draw()
	if power2.on:
		power2.Draw()
	if power3.on:
		power3.Draw()
	if power4.on:
		power4.Draw()


	plr.DrawObject()
	bad.DrawObject()
	GameClass.font.render_to(GameClass.window, ((1080/2) - 50, 20), GameClass.timestr, (255, 255, 255))

	game.display.update()
game.quit()
```
