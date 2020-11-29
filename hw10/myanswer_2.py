class Tictactoe:
	board = []
	def __init__(self):
		self.board = [[0 for _ in range(3)] for _ in range(3)]
	
	def play(self,color,x,y):
		if x < 0 or x > 2 or y < 0 or y > 2 or self.board[x][y] != 0:
			return False
		self.board[x][y] = color
		return True

	def win(self,color):
		if self.board[0][0] == color and self.board[0][1] == color and self.board[0][2] == color: return True
		if self.board[1][0] == color and self.board[1][1] == color and self.board[1][2] == color: return True
		if self.board[2][0] == color and self.board[2][1] == color and self.board[2][2] == color: return True
		if self.board[0][0] == color and self.board[1][0] == color and self.board[2][0] == color: return True
		if self.board[0][1] == color and self.board[1][1] == color and self.board[2][1] == color: return True
		if self.board[0][2] == color and self.board[1][2] == color and self.board[2][2] == color: return True
		if self.board[0][0] == color and self.board[1][1] == color and self.board[2][2] == color: return True
		if self.board[0][2] == color and self.board[1][1] == color and self.board[2][0] == color: return True
		return False

Colors = [1,2]
Moves = list(map(int, input().split(' ')))
TTT = Tictactoe()

for m in range(len(Moves)):
	if TTT.play(Colors[m%2],(Moves[m]-1)//3,(Moves[m]-1)%3) == False:
		print('illegal move')
		exit()
	if TTT.win(Colors[m%2]):
		print(Moves[m])
		exit()
print(0)