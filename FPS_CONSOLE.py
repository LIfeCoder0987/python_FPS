import math
from time import time
from win32 import win32console
from win32 import win32api

pyConsoleScreenBuffer = win32console.CreateConsoleScreenBuffer()
pyConsoleScreenBuffer.SetConsoleActiveScreenBuffer()
pycoord = win32console.PyCOORDType(0,0)

ScreenWidth = 120
ScreenHeight = 40

PlayerX = 8.0
PlayerY = 8.0
PlayerA = 0.0

FOV = math.pi / 4.0
Depth = 16.0

MapWidth = 16
MapHeight = 16

mapp = ""
mapp += "################"
mapp += "#..............#"
mapp += "#..............#"
mapp += "#..............#"
mapp += "#..........#...#"
mapp += "#..........#...#"
mapp += "#..............#"
mapp += "#..............#"
mapp += "#..............#"
mapp += "#..............#"
mapp += "#..............#"
mapp += "#..............#"
mapp += "#.......########"
mapp += "#..............#"
mapp += "#..............#"
mapp += "################"

screen = ''
for i in range(ScreenWidth*ScreenHeight):
	screen += ' '

def drawing_on_the_screen(screen, char, pos):
	screen = list(screen)
	screen[pos] = char
	return "".join(screen)

tp1 = time()
tp2 = time()

while True:

	tp2 = time()
	elapsedTime = tp2 - tp1
	tp1 = tp2

	t1 = time()
	t2 = time()
	
	if (win32api.GetAsyncKeyState(ord('Q') & ord('Q'))):
		PlayerA -= 0.1 * elapsedTime
	if (win32api.GetAsyncKeyState(ord('D') & ord('D'))):
		PlayerA += 0.1 * elapsedTime

	if (win32api.GetAsyncKeyState(ord('Z') & ord('Z'))):
		PlayerX += math.sin(PlayerA) * 2.0 * elapsedTime
		PlayerY += math.cos(PlayerA) * 2.0 * elapsedTime

	if (win32api.GetAsyncKeyState(ord('S') & ord('S'))):
		PlayerX -= math.sin(PlayerA) * 2.0 * elapsedTime
		PlayerY -= math.cos(PlayerA) * 2.0 * elapsedTime

	for x in range(ScreenWidth):
		RayAngle = (PlayerA - FOV / 2.0) + (x / ScreenWidth) * FOV

		DistanceToWall = 0
		HitWall = False

		EyeX = math.sin(RayAngle)
		EyeY = math.cos(RayAngle)

		while not HitWall and DistanceToWall < Depth:

			DistanceToWall += 0.1

			TestX = int(PlayerX + EyeX * DistanceToWall)
			TestY = int(PlayerX + EyeY * DistanceToWall)

			# Test if ray is out of bounds
			if TestX < 0 or TestX >= MapWidth or TestY < 0 or TestY >= MapHeight:
				HitWall = True
				DistanceToWall = Depth # just set distance to maximum depth
			else:
				# Ray is bounds so test to see if the ray cell is a wall block
				if mapp[TestY * MapWidth + TestX] == "#":
					HitWall = True

		# Calculate distance to ceiling and floor
		Ceiling = (ScreenHeight / 2.0) - ScreenHeight / DistanceToWall
		Floor = ScreenHeight - Ceiling

		Shade = ''

		if DistanceToWall <= Depth / 4.0:
			Shade = u"\U00002588"
		elif DistanceToWall < Depth / 3.0:
			Shade = u"\U00002593"
		elif DistanceToWall < Depth / 2.0:
			Shade = u"\U00002592"
		elif DistanceToWall < Depth:
			Shade = u"\U00002591"
		else:
			Shade = ' '

		for y in range(ScreenHeight):

			if y < Ceiling:
				screen = drawing_on_the_screen(screen, " ", y*ScreenWidth + x)
			elif y > Ceiling and y <= Floor:
				screen = drawing_on_the_screen(screen, Shade, y*ScreenWidth + x)
			else:
				screen = drawing_on_the_screen(screen, "-", y*ScreenWidth + x)

	pyConsoleScreenBuffer.WriteConsoleOutputCharacter(screen,pycoord)
	t2 = time()
	deltt = t2 - t1
	print(deltt)
	t1 = t2