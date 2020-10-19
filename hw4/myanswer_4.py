direction = ((0,2),(1,1),(1,-1),(0,-2),(-1,-1),(-1,1))
trap_route = []
trap_pos = [[0,0],[0,0],[0,0]]

def add(a,b):
	return a+b

def move_car(trap_pos,car_route):
	car_pos = [0,0]
	for d in car_route:
		car_pos = list(map(add,car_pos,direction[d]))
		for i in range(3):
			if car_pos == trap_pos[i]:
				return trap_pos[i]
	return car_pos

def distance(pos):
	x_dis = abs(pos[0]) 
	y_dis = abs(pos[1])
	y_dis = (y_dis-x_dis)//2 if y_dis-x_dis > 0 else 0
	return x_dis + y_dis

for i in range(3):
	trap_route.append(list(map(int,input().split(' '))))
	for d in trap_route[i]:
		trap_pos[i] = list(map(add,trap_pos[i],direction[d]))
	if trap_pos[i] == [0,0]:
		print(0)
		exit()
car_route = list(map(int,input().split(' ')))

car_pos = move_car(trap_pos,car_route)
#print(car_pos)
print(distance(car_pos))