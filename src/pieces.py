class Piece():
	def __init__(self, color, number, position):
		self.color = color
		self.number = number
		self.captured = False
		self.position = position

class Pawn(Piece):
	def info(self):
		return f'{self.color}p{self.number}'

class Rook(Piece):
	def __init__(self, color, number, position):
		super().__init__(color, number, position);
		self.canCastle = 1
	def info(self):
		return f'{self.color}r{self.number}'

class Knight(Piece):
	def info(self):
		return f'{self.color}n{self.number}'

class Bishop(Piece):
	def info(self):
		return f'{self.color}b{self.number}'

class Queen(Piece):
	def info(self):
		return f'{self.color}q{self.number}'

class King(Piece):
	def __init__(self, color, number, position):
		super().__init__(color, number, position);
		self.canCastle = 1;
		self.isInCheck = 0;
	def info(self):
		return f'{self.color}k{self.number}'

board = [[None for i in range(8)] for j in range(8)]

def pieceList():
	plist = [[None for i in range(16)] for j in range(2)]

	# Add pawns to piece list and board
	for i in range(8):
		plist[0][i] = Pawn('b', i+1, [1,i])
		board[1][i] = plist[0][i]

		plist[1][i] = Pawn('w', i+1, [6,i])
		board[6][i] = plist[1][i]
    
	# Add rooks to piece list and board
	plist[0][8] = Rook('b', 1, [0,0])
	plist[0][9] = Rook('b', 2, [0,7])
	board[0][0] = plist[0][8]
	board[0][7] = plist[0][9]

	plist[1][8] = Rook('w', 1, [7,0])
	plist[1][9] = Rook('w', 2, [7,7])
	board[7][0] = plist[1][8]
	board[7][7] = plist[1][9]

	# Add knights to piece list and board
	plist[0][10] = Knight('b', 1, [0,1])
	plist[0][11] = Knight('b', 2, [0,6])
	board[0][1] = plist[0][10]
	board[0][6] = plist[0][11]

	plist[1][10] = Knight('w', 1, [7,1])
	plist[1][11] = Knight('w', 2, [7,6])
	board[7][1] = plist[1][10]
	board[7][6] = plist[1][11]

	# Add bishops to piece list and board
	plist[0][12] = Bishop('b', 1, [0,2])
	plist[0][13] = Bishop('b', 2, [0,5])
	board[0][2] = plist[0][12]
	board[0][5] = plist[0][13]

	plist[1][12] = Bishop('w', 1, [7,2])
	plist[1][13] = Bishop('w', 2, [7,5])
	board[7][2] = plist[1][12]
	board[7][5] = plist[1][13]

	# Add queens to piece list and board
	plist[0][14] = Queen('b', 1, [0,3])
	board[0][3] = plist[0][14]

	plist[1][14] = Queen('w', 1, [7,3])
	board[7][3] = plist[1][14]

	# Add kings to piece list and board
	plist[0][15] = King('b', 1, [0,4])
	board[0][4] = plist[0][15]

	plist[1][15] = King('w', 1, [7,4])
	board[7][4] = plist[1][15]

	return plist
