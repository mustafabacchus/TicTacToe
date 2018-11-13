board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 1


def print_board():
    cur_board = ''
    for row in range(len(board)):
        cur_board += '\n'
        for col in range(len(board[row])):
            cur_board += str(board[row][col]) + '  '
    # Remove empty line return
    cur_board = cur_board[1:]
    print cur_board


def define_mark():
    # Player X: Odd, Player O: Even
    # Determine marker type
    if player % 2 == 0:
        marker = 'O'
    else:
        marker = 'X'
    return marker


def place_mark():
    # Get user input values
    while True:
        while True:
            try:
                row = int(raw_input('Select Row: '))
                if row > 2:
                    raise ValueError
                break
            except ValueError:
                print 'Row does not exist, try again.'
        while True:
            try:
                col = int(raw_input('Select Column: '))
                if col > 2:
                    raise ValueError
                break
            except ValueError:
                print 'Column does not exist, try again.'
        # Place mark
        if board[row][col] == ' ':
            board[row][col] = define_mark()
            break
        else:
            print 'Space occupied, try again.'
            print ''


def check_wins():
    mark = define_mark() * 3
    # Rows
    val = ''
    for row in range(len(board)):
        for col in range(len(board[row])):
            val += str(board[row][col])
    if val[:3] == mark or val[3:6] == mark or val[6:] == mark:
        return True
    # Columns
    val = ''
    for row in range(len(board)):
        for col in range(len(board[row])):
            val += str(board[col][row])
    if val[:3] == mark or val[3:6] == mark or val[6:] == mark:
        return True
    # Left Top to Right Bottom Diagonal
    val = ''
    for row in range(len(board)):
        col = row
        val += str(board[row][col])
    if val == mark:
        return True
    # Right Top to Left Bottom Diagonal
    val = ''
    for row in range(len(board)):
        col = (len(board) - 1) - row
        val += str(board[row][col])
    if val == mark:
        return True
    return False


def play():
    global player
    print 'TIC TAC TOE: BEGIN!'
    # Print initial blank board
    print ''
    print_board()
    print ''
    while True:
        place_mark()
        # Print board
        print ''
        print_board()
        print ''
        # Win event
        if check_wins() is True:
            print 'GAME OVER: PLAYER ' + define_mark() + ' WINS!'
            break
        # Tie event
        if player == 9:
            print 'GAME OVER: TIE!'
            break
        player += 1


play()
