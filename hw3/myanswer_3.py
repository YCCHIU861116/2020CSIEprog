s = input()
l = len(s)

maxbegin = 101
maxend = -101
maxlength = 0

for begin in range(l):
	for end in range(begin+2,l+1):
		length = end - begin
		if(length%2 == 1):
			continue;
		if(s[begin:begin+length//2] == s[begin+length//2:end] and length > maxlength):
			maxbegin = begin
			maxend = end
			maxlength = length
print(s[maxbegin:maxend])