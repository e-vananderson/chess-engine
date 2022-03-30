class Piece():
	def __init__(self, color, number, position):
		self.color = color
		self.number = number
		self.bitboard = array('B', [0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0])
		self.bitboard[position] = 1;

class Pawn(Piece):
	pass

class Rook(Piece):
	def __init__(self, color, number, position):
		super().__init__(color, number, position);
		self.canCastle = 1

class Knight(Piece):
	pass

class Bishop(Piece):
	pass

class Queen(Piece):
	pass

class King(Piece):
	def __init__(self, color, number, position):
		super().__init__(color, number, position);
		self.canCastle = 1;
		self.isInCheck = 0;
