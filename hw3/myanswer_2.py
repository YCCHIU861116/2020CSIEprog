s = [input() for i in range(2)]
N = len(s[0])
junc = [[],[]]

for t in range(2):
	before = s[t][0]
	for i in range(1,N):
		now = s[t][i]
		if before != now:
			junc[t].append(i-1)
		before = now
#print(junc)

it = [0,0]
mindifference = 10001
minindex = [-1,-1]
while it[0] < len(junc[0]) and  it[1] < len(junc[1]):
	difference = abs(junc[0][it[0]]-junc[1][it[1]])
	if(difference < mindifference):
		mindifference = difference
		minindex[0],minindex[1] = junc[0][it[0]],junc[1][it[1]]

	if(junc[0][it[0]] < junc[1][it[1]]):
		it[0]+=1;
	elif(junc[0][it[0]] > junc[1][it[1]]):
		it[1]+=1;
	else:
		break;
for i in range(2):
	print(minindex[i]+1)