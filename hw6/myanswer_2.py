number = [str(i) for i in range(10)]
sign = ['+','-']
def isint(s):
	if s[0] in sign:
		s = s[1:]
	if len(s) == 0:
		return False
	for c in s:
		if c not in number:
			return False
	return True

def isfloat(s):
	if s[0] in sign:
		s = s[1:]
	dot = s.find('.')
	if dot == len(s)-1 or dot == -1:
		return False
	for i in range(len(s)):
		if i == dot:
			continue
		if s[i] not in number:
			return False
	return True

def isefloat(s):
	# if s[0] in sign:
	# 	s = s[1:]
	e = s.find('e')
	if e == -1 or e == 0 or e == len(s)-1:
		return False
	return (isint(s[:e]) or isfloat(s[:e])) and isint(s[e+1:])

def type_judge(s):
	if isint(s):
		return 'int'
	elif isfloat(s):
		return 'float'
	elif isefloat(s):
		return 'float'
	else:
		return 'str'

n = eval(input())
for _ in range(n):
	s = input()
	print(type_judge(s))