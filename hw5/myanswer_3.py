N = eval(input())

for _ in range(N):
	answer, G = input().split(' ')
	G = eval(G)
	guess = input()
	nowstr = '*'*len(answer)

	g = 0
	result = -1
	for c in guess:
		if answer.find(c) == -1:
			g += 1
			if g == G:
				print(-1, nowstr, sep=' ')
				print('You Lose')
				result = 0
				break
			else:
				print(0, nowstr,sep=' ')
		else:
			start = 0
			find = 0
			while find != -1:
				find = answer.find(c,start)
				if find != -1:
					start = find + 1
					nowstr = nowstr[:find]+c+nowstr[find+1:]
			print(1,nowstr,sep=' ')
		if nowstr == answer:
			print('You Win')
			result = 1
			break
	if result == -1:
		print('You Quit')