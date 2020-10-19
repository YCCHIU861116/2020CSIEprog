def addcountercheck(mask,counter,pos,n):
	for i in range(len(mask)):
		if mask[i][pos]:
			counter[i] += 1
			if counter[i] == n:
				return 1
	return 0

n = eval(input())
N =n**3
cube = list(range(N))
draw = list(range(N))
bingo = [1 for i in range(n)]
mask = []

for i in range(n*n):
	line = input().split(' ')
	for j in range(n):
		cube[int(line[j])-1] = i*n+j

for i in range(n*n):
	line = input().split(' ')
	for j in range(n):
		draw[i*n+j] = int(line[j])

for i in range(n*n):
	mask.append([(pos//n == i) for pos in range(N)]) #if j in [i*n + j for j in range(n)]straightx
	mask.append([pos//(n*n) == i//n and pos%n == i%n for pos in range(N)])			#straighty				
	mask.append([pos%(n*n) == i for pos in range(N)])								#straightz
for i in range(n):
	mask.append([pos//(n*n) == i and (pos//n)%n == pos%n			for pos in range(N)])	#diagon_xy_cis = 
	mask.append([pos//(n*n) == i and (pos//n)%n + pos%n == n-1		for pos in range(N)])	#diagon_xy_trans =
	mask.append([(pos%(n*n))//n == i and pos//(n*n) == pos%n 		for pos in range(N)])	#diagon_xz_cis =
	mask.append([(pos%(n*n))//n == i and pos//(n*n) + pos%n ==n-1	for pos in range(N)])	#diagon_xz_trans =  
	mask.append([pos%n == i and pos//(n*n) == (pos//n)%n 			for pos in range(N)])	#diagon_yz_cis = 
	mask.append([pos%n == i and pos//(n*n) + (pos//n)%n	 ==	n-1		for pos in range(N)]) #diagon_yz_trans = 
mask.append([pos%(n*n+n+1) == 0			for pos in range(N)])	#diagon_xyz_0  
mask.append([pos%(n*n+n-1) == n-1		for pos in range(N)])	#diagon_xyz_1
mask.append([pos%(n*n-n+1) == n*n-n 	for pos in range(N)])	#diagon_xyz_2
mask.append([pos%(n*n-n-1) == n and pos !=n and pos != n**3-n-1 for pos in range(N)]) #diagon_xyz_3

line_num = len(mask)
counter = [0 for i in range(line_num)]

for i in range(N):
	if(addcountercheck(mask,counter,cube[draw[i]-1],n)):
		print(draw[i])
		exit()