def check_and_insert(dic,c):
	value = dic.get(c)
	if value == None:
		dic[c] = 1
	else:
		dic[c] += 1

def string_similarity(s1,s2):
	a = 0
	b = 0
	dic1 = {}
	dic2 = {}
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			a+=1
		else:
			check_and_insert(dic1,s1[i])
			check_and_insert(dic2,s2[i])
	for key in dic1:
		value = dic2.get(key)
		if value != None:
			b += min(value,dic1[key])
	#print(dic1,dic2)
	return a,b

s1 = input()
s2 = input()

A,B = string_similarity(s1,s2)
print(A)
print(B)