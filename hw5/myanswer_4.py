N = eval(input())
array = list(map(int,input().split(' ')))

max_ending_here = max_so_far = 0
max_ending_here_begin = 0
max_begin = 0
max_end = 0
for i in range(len(array)):
	if(max_ending_here + array[i] >= 0):
		max_ending_here = max_ending_here + array[i]
	else:
		max_ending_here = 0
		max_ending_here_begin = i+1
	if(max_ending_here > max_so_far):
		max_so_far = max_ending_here
		max_begin = max_ending_here_begin
		max_end = i+1
#print(max_so_far)
print(max_begin)
print(max_end)