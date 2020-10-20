def road_judge(city):
	n = len(city)
	for i in range(n):
		city[i].insert(0,0)
		city[i].append(0)
	city.insert(0,[0 for i in range(n+2)])
	city.append([0 for i in range(n+2)])

	ix,T,t,d = 0,0,0,0
	for i in range(1,n+1):
		for j in range(1,n+1):
			if city[i][j]:
				neighbor = city[i+1][j]+city[i-1][j]+city[i][j+1]+city[i][j-1]
				ix += 1 if neighbor == 4 else 0
				T += 1 if neighbor == 3 else 0
				t += 1 if neighbor == 2 and city[i+1][j]^city[i-1][j] else 0
				d += 1 if neighbor == 1 else 0
	return ix,T,t,d

city = []
n = eval(input())
for i in range(n):
	city.append(list(map(int,input().split(' '))))
i,T,t,d = road_judge(city)
print(i)
print(T)
print(t)
print(d)