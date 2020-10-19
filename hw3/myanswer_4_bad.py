n = eval(input())
N =n*n*n
cube = list(range(N))
draw = list(range(N))
choosed = [0 for i in range(N)]
bingo = [1 for i in range(n)]

def check(x):
	return x == bingo

def check_bingo(choosed,n):
	for i in range(n*n):
		if check([c for pos ,c in enumerate(choosed) if pos//n == i]): 										return 1 #straightx#if pos in [i*n + j for j in range(n)]straightx
		if check([c for pos ,c in enumerate(choosed) if pos//(n*n) == i//n and pos%n == i%n]):				return 2 #straighty
		if check([c for pos ,c in enumerate(choosed) if pos%(n*n) == i]):									return 3 #straightz = 
	for i in range(n):
		if check([c for pos ,c in enumerate(choosed) if pos//(n*n) == i and (pos//n)%n == pos%n]):			return 4#diagon_xy_cis = 
		if check([c for pos ,c in enumerate(choosed) if pos//(n*n) == i and (pos//n)%n + pos%n == n-1]):	return 5#diagon_xy_trans = 
		if check([c for pos ,c in enumerate(choosed) if (pos%(n*n))//n == i and pos//(n*n) == pos%n]):		return 6#diagon_xz_cis = 
		if check([c for pos ,c in enumerate(choosed) if (pos%(n*n))//n == i and pos//(n*n) + pos%n == n-1]):	return 7#diagon_xz_trans = 
		if check([c for pos ,c in enumerate(choosed) if pos%n == i and pos//(n*n) == (pos//n)%n]): 			return 8#diagon_yz_cis = 
		if check([c for pos ,c in enumerate(choosed) if pos%n == i and pos//(n*n) + (pos//n)%n == n-1]): 			return 9#diagon_yz_trans = 
	if check([c for pos ,c in enumerate(choosed) if pos%(n*n+n+1) == 0]): 									return 10#diagon_xyz_0 = 
	if check([c for pos ,c in enumerate(choosed) if pos%(n*n+n-1) == n-1]):								return 11#diagon_xyz_1
	if check([c for pos ,c in enumerate(choosed) if pos%(n*n-n+1) == n*n-n]): 	return 12  #diagon_xyz_2
	if check([c for pos ,c in enumerate(choosed) if pos%(n*n-n-1) == n and pos !=n and pos != n**3-n-1]): 	return 13 #diagon_xyz_3 =
	return 0

for i in range(n*n):
	line = input().split(' ')
	for j in range(n):
		cube[int(line[j])-1] = i*n+j

for i in range(n*n):
	line = input().split(' ')
	for j in range(n):
		draw[i*n+j] = int(line[j])

for i in range(N):
	choosed[cube[draw[i]-1]] = 1
	if i >= n-1:
		if(check_bingo(choosed,n)):
			print(draw[i])
			break;

# print(cube) 
# print(draw)