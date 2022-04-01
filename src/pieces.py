class Piece():
	def __init__(self, color, position):
		self.color = color
        self.captured = false
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
	def __init__(self, color, position):
		super().__init__(color, position);
		self.canCastle = 1

class Knight(Piece):
	pass

class Bishop(Piece):
	pass

class Queen(Piece):
	pass

class King(Piece):
	def __init__(self, color, position):
		super().__init__(color, position);
		self.canCastle = 1;
		self.isInCheck = 0;

def pieceList():
    Piece plist[2][16]

    for i in range(8):
        plist[0][i] = Pawn('w', [1,i])
        plist[1][i] = Pawn('b', [6,i])
    
    plist[0][8] = Rook('w', [0,0])
    plist[1][8] = Rook('b', [7,0])

    plist[0][9] = Bishop('w', [0,1])
    plist[1][9] = Bishop('b', [7,1])

    plist[0][10] = Knight('w', [0,2])
    plist[1][10] = Knight('b', [7,2])

    plist[0][11] = Queen('w', [0,3])
    plist[1][11] = Queen('b', [7,3])

    plist[0][12] = King('w', [0,4])
    plist[1][12] = King('b', [7,4])

    plist[0][13] = Bishop('w', [0,5])
    plist[1][13] = Bishop('b', [7,5])

    plist[0][14] = Knight('w', [0,6])
    plist[1][14] = Knight('b', [7,6])

    plist[0][15] = Rook('w', [0,7])
    plist[1][15] = Rook('b', [7,7])

    return plist
