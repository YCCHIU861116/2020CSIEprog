def tiles(types,x,y,m):
	if m == 1:
		print(types,x,y)
		return
	tiles(types,x,y,m//2)
	if types != 1: tiles(3,x+m//2,y+m//2,m//2)
	if types != 2: tiles(4,x-m//2,y+m//2,m//2)
	if types != 3: tiles(1,x-m//2,y-m//2,m//2)
	if types != 4: tiles(2,x+m//2,y-m//2,m//2)

l,m = list(map(int,input().split(' ')))
center_pos = l//2
it = m

while l >= 2*it:
	tiles(1,center_pos,center_pos,(l//2)//(it//m))
	center_pos += (l - center_pos)//2
	it *= 2