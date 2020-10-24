def how_many_ways(matrix,x,y,m):
	if matrix[x][y] == 0:
		return 0
	if x == 0 and y == m-1:
		return 1
	if x == 0:
		return how_many_ways(matrix,0,y+1,m)
	if y == m-1:
		return how_many_ways(matrix,x-1,m-1,m)
	return how_many_ways(matrix,x,y+1,m) + how_many_ways(matrix,x-1,y,m)

n,m= tuple(map(int,input().split(' ')))
matrix = []
for i in range(n):
	matrix.append(list(map(int,input().split(' '))))
#print(matrix)
print(how_many_ways(matrix,n-1,0,m))