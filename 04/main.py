with open('input.txt') as f:
    lines = f.readlines()
    order = list(map(int, lines[0].split(',')))
    
    boards = []
    board = []
    for line in lines[2:]:
        line = line.strip()
        if not line:
            boards.append(board)
            board = []
        else:
            board.append(list(map(int, line.split())))

    n = 0
    bingo = False
    bingo_board = None
    for i in range(6, len(order)):
        n = order[i - 1]
        for board in boards:
            for row in board:
                for j, num in enumerate(row):
                    if num in order[:i]:
                        row[j] = -1
                     
        for board in boards:
            for row in board:
                if all(x == -1 for x in row):
                    bingo = True
                    bingo_board = board
                    
            for col in range(5):
                if all(row[col] == -1 for row in board):
                    bingo = True
                    bingo_board = board
                    
            if bingo:
                break

        if bingo:
            break
            
    b = sum(x for row in bingo_board for x in row  if x != -1)

    for row in bingo_board:
        print(row)
    print(b, n, n * b)


with open('input.txt') as f:
    lines = f.readlines()
    order = list(map(int, lines[0].split(',')))
    
    boards = []
    board = []
    for line in lines[2:]:
        line = line.strip()
        if not line:
            boards.append(board)
            board = []
        else:
            board.append(list(map(int, line.split())))

    n = 0
    bingo = False
    bingo_board = None
    won = len(boards) * [0]
    for i in range(6, len(order)):
        n = order[i - 1]
        for board in boards:
            for row in board:
                for j, num in enumerate(row):
                    if num in order[:i]:
                        row[j] = -1
                     
        for j, board in enumerate(boards):
            if won[j]:
                continue
        
            for row in board:
                if all(x == -1 for x in row):
                    won[j] = 1
                    bingo_board = board
                    
            for col in range(5):
                if all(row[col] == -1 for row in board):
                    won[j] = 1
                    bingo_board = board

        if sum(won) == len(boards):
            break
            
    b = sum(x for row in bingo_board for x in row  if x != -1)

    for row in bingo_board:
        print(row)
    print(b, n, n * b)
