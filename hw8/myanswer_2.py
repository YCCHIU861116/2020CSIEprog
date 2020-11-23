alphabet = '0123456789abcdefgh'
def printtable(stage_num,Table):
	for i in range(stage_num):
		print(*Table[i*stage_num:(i+1)*stage_num])

def collide(x,y):
	return (x[0] == y[0] or x[0] == y[1] or x[1] == y[0] or x[1] == y[1])

def is_available(stage_num,Table,test):
	T = len(Table)
	stage = T % stage_num
	for t in range(stage,T,stage_num):
		if collide(Table[t],test):
			return 0
	for grid in Table:
		if test == grid:
			return 0
	return 1

def RPG(team_num,stage_num,Table,team,XX_num):
	T = len(Table)
	if T == stage_num**2:
		printtable(stage_num,Table)
		exit()
	if T % stage_num == 0:
		team = [alphabet[i] for i in range(team_num)]
		XX_num = stage_num - team_num//2
	
	now_team_num = len(team)
	for i in range(now_team_num):
		for j in range(i+1,now_team_num):
			if is_available(stage_num,Table,team[i]+team[j]):
				New_Table = [grid[:] for grid in Table]
				New_team = team.copy()
				New_Table.append(team[i]+team[j])
				New_team.pop(j)
				New_team.pop(i)
				RPG(team_num,stage_num,New_Table,New_team,XX_num)
	if XX_num > 0:
		XX_num -= 1
		New_Table = [grid[:] for grid in Table]
		New_team = team.copy()
		New_Table.append('xx')
		RPG(team_num,stage_num,New_Table,New_team,XX_num)

team_num = eval(input())
stage_num = eval(input())
Table = [alphabet[2*i:2*i+2] for i in range(team_num//2)]
for i in range(stage_num - team_num//2): Table.append('xx')
team = [alphabet[i] for i in range(team_num)]
if team_num > 4 and stage_num > 2:
	Table.append('24')
	team.remove('2')
	team.remove('4')
XX_num = stage_num - team_num//2
RPG(team_num,stage_num,Table,team,XX_num)
print(-1)