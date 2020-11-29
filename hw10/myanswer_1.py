class SQLServer:
	def __init__(self):
		self.Guestlist = []

	def addGuest(self,addstr):
		Fieldkeys = ['lastname','firstname','ID','salary','age']
		Newguest = addstr.split(' ')
		guest_field = dict([(Fieldkeys[i],Newguest[i]) if i < 3 else (Fieldkeys[i],int(Newguest[i])) for i in range(5)])
		self.Guestlist.append(guest_field)

	def selectGuest(self,selectstr):
		operator = {'==' : (lambda x,y: x == y), '!=': (lambda x,y: x != y),'>': (lambda x,y: x > y),'<': (lambda x,y: x < y),}
		i = 1
		words = selectstr.split(' ')
		Goal_field = []
		while words[i] != 'where':
			Goal_field.append(words[i])
			i += 1
		for guest in self.Guestlist:
			constant = int(words[i+3]) if words[i+1] == 'salary' or words[i+1] == 'age' else words[i+3]
			if operator[words[i+2]](guest[words[i+1]],constant): 
				print(*[guest[goal] for goal in Goal_field])

S = SQLServer()

for _ in range(int(input())):
	S.addGuest(input())

for _ in range(int(input())):
	S.selectGuest(input())