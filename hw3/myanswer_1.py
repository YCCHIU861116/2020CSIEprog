def gcd(a,b):
	return a if(b==0) else gcd(b,a%b)
def lcm(a,b):
	return abs(a*b//gcd(a,b))
def reduction(a,b):
	gcd_reduct = abs(gcd(a,b))
	a //= gcd_reduct
	b //= gcd_reduct
	return a,b
def transfer(deno,deci):
	h = deno // deci if(deno>0) else -(-deno //deci)
	i = deno % deci if(deno>0) else -deno %deci
	j = deci
	return h,i,j

def add(deno1,deno2,deci1,deci2):
	deci = lcm(deci1,deci2)
	deno = deno1 * (deci//deci1) + deno2 * (deci//deci2)
	deno,deci = reduction(deno,deci)
	return transfer(deno,deci)
def sub(deno1,deno2,deci1,deci2):
	return add(deno1,-deno2,deci1,deci2)
def mul(deno1,deno2,deci1,deci2):
	deno = deno1*deno2
	deci = deci1*deci2
	deno,deci = reduction(deno,deci)
	return transfer(deno,deci)
def div(deno1,deno2,deci1,deci2):
	rdeno2 = (deci2 if (deno2>0) else -deci2)
	rdeci2 = (deno2 if(deno2>0) else -deno2)
	return mul(deno1,rdeno2,deci1,rdeci2)

a,b,c,d,e,f,g = [eval(input()) for i in range(7)]

deno1 = a*c+b if a > 0 else a*c-b
deno2 = e*g+f if e > 0 else e*g-f
deci1 = c
deci2 =	g

Operator = {
	0:add,
	1:sub,
	2:mul,
	3:div
}
h,i,j = Operator[d](deno1,deno2,deci1,deci2)
print(h)
print(i)
print(j)