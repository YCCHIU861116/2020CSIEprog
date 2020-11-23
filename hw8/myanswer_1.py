FIELD_LEN = 9
FIELD_SIZE = FIELD_LEN**2

def printMine(Mine):
	for i in range(1,FIELD_LEN+1):
		print(*(Mine[i][1:FIELD_LEN+1]))

def checkminenum(Field,Mine,pos):
	x = pos//FIELD_LEN
	y = pos%FIELD_LEN
	Minenum = 0
	for i in range(3):
		for j in range(3):
			Minenum += Mine[x+i][y+j]
	return Field[x][y] - Minenum

def Origin(Field,Mine,pos):
	if Field[0][0] == 0:
		FindMine(Field,Mine,pos+1)
	elif Field[0][0] == 1:
		for i in range(4):
			Mine[1+i//2][1+i%2] = 1
			FindMine(Field,Mine,pos+1)
			Mine[1+i//2][1+i%2] = 0
	elif Field[0][0] == 2:
		for i in range(4):
			Mine[1+i//2][1+i%2] = 1
			for j in range(i+1,4):
				Mine[1+j//2][1+j%2] = 1
				FindMine(Field,Mine,pos+1)
				Mine[1+j//2][1+j%2] = 0
			Mine[1+i//2][1+i%2] = 0
	elif Field[0][0] == 3:
		Mine[1][1] = Mine[1][2] = Mine[2][1] = Mine[2][2] = 1
		for i in range(4):
			Mine[1+i//2][1+i%2] = 0
			FindMine(Field,Mine,pos+1)
			Mine[1+i//2][1+i%2] = 1
		Mine[1][1] = Mine[1][2] = Mine[2][1] = Mine[2][2] = 0
	else:
		Mine[1][1] = Mine[1][2] = Mine[2][1] = Mine[2][2] = 1
		FindMine(Field,Mine,pos+1)

def Upperline(Field,Mine,pos):
	Minenum = checkminenum(Field,Mine,pos)
	if Minenum < 0 or Minenum > 2: return
	y = pos%FIELD_LEN+1
	if Minenum == 0:
		FindMine(Field,Mine,pos+1)
	elif Minenum == 1:
		for i in range(2):
			Mine[1+i%2][y+1]= 1
			FindMine(Field,Mine,pos+1)
			Mine[1+i%2][y+1]= 0
	else:
		Mine[1][y+1] = Mine[2][y+1] = 1
		FindMine(Field,Mine,pos+1)
		Mine[1][y+1] = Mine[2][y+1] = 0

def Leftline(Field,Mine,pos):
	Minenum = checkminenum(Field,Mine,pos)
	if Minenum < 0 or Minenum > 2: return
	x = pos//FIELD_LEN+1
	if Minenum == 0:
		FindMine(Field,Mine,pos+1)
	elif Minenum == 1:
		for i in range(2):
			Mine[x+1][1+i%2]= 1
			FindMine(Field,Mine,pos+1)
			Mine[x+1][1+i%2]= 0
	else:
		Mine[x+1][1] = Mine[x+1][2] = 1
		FindMine(Field,Mine,pos+1)
		Mine[x+1][1] = Mine[x+1][2] = 0

def Middle(Field,Mine,pos):
	Minenum = checkminenum(Field,Mine,pos)
	if Minenum < 0 or Minenum > 1: return
	x = pos//FIELD_LEN+1
	y = pos%FIELD_LEN+1
	if Minenum == 0:
		FindMine(Field,Mine,pos+1)
	else:
		Mine[x+1][y+1] = 1
		FindMine(Field,Mine,pos+1)
		Mine[x+1][y+1] = 0

def FindMine(Field,Mine,pos):
	if pos == FIELD_SIZE:
		printMine(Mine)
		exit()
	if pos == 0:
		Origin(Field,Mine,pos)
	elif pos > 0 and pos < FIELD_LEN-1:
		Upperline(Field,Mine,pos)
	elif pos // FIELD_LEN != FIELD_LEN-1 and pos % FIELD_LEN == 0:
		Leftline(Field,Mine,pos)
	elif pos // FIELD_LEN != FIELD_LEN-1 and pos % FIELD_LEN != FIELD_LEN-1:
		Middle(Field,Mine,pos)
	else:
		if checkminenum(Field,Mine,pos) != 0:
			return
		else:
			FindMine(Field,Mine,pos+1)

Field = []
Mine = [[0 for _ in range(FIELD_LEN+2)] for _ in range(FIELD_LEN+2)]

for i in range(FIELD_LEN):
	Field.append([int(a) for a in input().split(' ')])
FindMine(Field,Mine,0)
print("no solution")