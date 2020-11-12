def permutation(permutate,to_be_choice):
	if to_be_choice == []:
		print(*permutate)
		return
	for i in range(len(to_be_choice)):
		permutate.append(to_be_choice.pop(i))
		permutation(permutate,to_be_choice)
		to_be_choice.insert(i,permutate.pop())

N = eval(input())
to_be_choice = list(map(int,input().split(' ')))
permutation([],sorted(to_be_choice))