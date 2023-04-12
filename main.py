from board import BoardSudoku

board = BoardSudoku()

board.upload_arq("puzzle_board/board1.txt")
board.display()
while not board.check():

    coord = input("|| Informe as coordenadas (x,y): ")
    moviment_x, moviment_y = map(int, coord.split(","))
    valor = int(input("|| Informe o valor: "))

    board.insert(moviment_x, moviment_y, valor)

board.display()
print("Parabéns")
