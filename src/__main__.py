import pieces

def main():
	plist = pieces.pieceList()
	for i in pieces.board:
		for j in i:
			if j == None:
				print("  0", end = ' ')
			else: 
				print(j.info(), end = ' ')
		print('')

if __name__ == '__main__':
	main()
