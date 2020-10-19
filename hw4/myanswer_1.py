def add(a,b):
	return a+b
def mul(a,b):
	return a*b

direction_table = ((0,10),(-10,0),(0,-10),(10,0))
command_dic= {1:1,2:-1,3:-1,5:2}

N = int(input())
stop = 0
direction = 0
pos = [0,0]
before_time = 0
for i in range(N):
	time = int(input())
	duration =  0 if stop else time - before_time
	before_time = time

	diff = list(map(mul,direction_table[direction],[duration,duration]))
	pos = list(map(add,pos,diff))

	command = int(input())
	if command in [1,2,5]:
		direction = (direction+command_dic[command])%4
	else:
		stop = 1 if command == 3 else 0 
print(pos[0])
print(pos[1])