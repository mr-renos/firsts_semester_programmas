from random import choice

board = []
rows = ["A","B","C","D","E","F","G","H"]
columns = [1,2,3,4,5,6,7,8]
#Will help me in finding the diagonal
valuesgrammatwn = columns[:]
pontoi_leukwn = 0
pontoi_mavrwn = 0

#Chess board
for i in rows:
    for j in columns:
        board.append([i,j])

for i in range(100):
    queen = choice(board)
    bishop = choice(board)
    while bishop == queen:
        bishop = choice(board)
    rook = choice(board)
    while rook == bishop or rook == queen:
        rook = choice(board)

    #When rook eats queen
    if rook[0] == queen[0] or rook[1] == queen[1]:
        pontoi_leukwn += 1

    #When bishop eats queen
    cola = rows.index(queen[0])
    colb = rows.index(bishop[0])
    if abs(queen[1] - bishop[1]) == abs(cola - colb):
        pontoi_leukwn += 1

    #When queen eats rook
    diaga = rows.index(queen[0])
    diagb = rows.index(rook[0])
    if rook[0] == queen[0] or rook[1] == queen[1] or abs(queen[1] - rook[1]) == abs(diaga - diagb):
        pontoi_mavrwn += 1

    #When queen eats bishop
    if abs(queen[1] - bishop[1]) == abs(cola - colb) or bishop[0] == queen[0] or bishop[1] == queen[1]:
        pontoi_mavrwn += 1

#Results
print("Black's points are: " + str(pontoi_mavrwn))
print("White's points are: " + str(pontoi_leukwn))

