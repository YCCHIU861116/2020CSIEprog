n = eval(input())
A = list(map(int,input().split(' ')))
m = eval(input())
B = list(map(int,input().split(' ')))
Q = []
R = A

for i in range(n-m+1):
	q0 = R[0]//B[0]
	Q.append(q0)
	for j in range(m):
		#print(i+j)
		R[j] -= q0 * B[j]
	R.remove(0)

if R == []:
	R = [0]
else:
	while R[0] == 0:
		R.remove(0)

print(*Q)
print(*R)