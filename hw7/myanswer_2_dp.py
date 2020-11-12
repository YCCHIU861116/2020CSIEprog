W,H = map(int,input().split(' '))

#whlist = []
Table = [[0 for _ in range(W+1)] for _ in range(H+1)]
for i in range(3):
	Input = input().split(' ')
	#whlist.append([eval(Input[0]),eval(Input[1])])
	w,h = eval(Input[0]),eval(Input[1])
	Table[h][w] = w*h

for h in range(1,H+1):
	for w in range(1,W+1):
		if Table[h][w] > 0: continue
		maxprice = 0
		for cut in range(1,w//2+1):
			price = Table[h][cut] + Table[h][w-cut] 
			maxprice = max(price,maxprice)
		for cut in range(1,h//2+1):
			price  = Table[cut][w] + Table[h-cut][w]
			maxprice = max(price,maxprice)
		Table[h][w] = maxprice
print(Table[H][W])