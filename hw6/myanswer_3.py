change_dir = {(0,1):(-1,0),(-1,0):(0,1),(1,0):(0,-1),(0,-1):(1,0)}

W,D= tuple(map(int,input().split(' ')))
house = []
for i in range(D):
	house.append(list(map(int,input().split(' '))))
num_to_pos_dir = {}

for i in range(2*W+2*D):
	if i < W:
		num_to_pos_dir[i] = ((i,D-1),(0,-1))
	elif i >= W and i < W + D:
		num_to_pos_dir[i] = ((W-1,W+D-i-1),(-1,0))
	elif i >= W+D and i < 2*W + D:
		num_to_pos_dir[i] = ((2*W+D-i-1,0),(0,1))
	else:
		num_to_pos_dir[i] = ((0,i-2*W-D),(1,0))

for i in range(2*W+2*D):
	pos = list(num_to_pos_dir[i][0])
	direction = num_to_pos_dir[i][1]
	while pos[0] < W and pos[0] >= 0 and pos[1] < D and pos[1] >= 0:
		if house[pos[1]][pos[0]]:
			direction = change_dir[direction]
		pos[0] += direction[0]
		pos[1] += direction[1]
	if pos[0] < 0:
		print(pos[1]+2*W+D)
	elif pos[0] >= W:
		print(W+D-1-pos[1])
	elif pos[1] < 0:
		print(2*W+D-1-pos[0])
	elif pos[1] >= D:
		print(pos[0])