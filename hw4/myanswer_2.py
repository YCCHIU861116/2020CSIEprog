import sys
fusion= ''
for line in sys.stdin:
	s = line[:-1]
	length = min(len(fusion),len(s))
	#print(fusion,s,length,list(range(length,0,-1)))
	for i in range(length,0,-1):
		if fusion[-i:] == s[:i]:
			fusion += s[i:]
			break
	else:
		fusion += s
print(fusion)