def bingo(gameboards, numbers):
    # store all numbers that are drawn for score calculation
    numbers_drawn = {}

    # numbers to draw
    for num in numbers:
        numbers_drawn[num] = 1

        # check all gameboards for number
        for i,board in enumerate(gameboards):
            board_dict = board[0]

            if num in board_dict:
                for row,col in board_dict[num]:
                    board[1][row] += 1
                    board[2][col] += 1

                    if board[1][row] == 5 or board[2][col] == 5:
                        compute_score(board_dict, numbers_drawn, num, i)
                        return


def compute_score(board, numbers_drawn, last_drawn_number, gameboard_number):
    print('winning_gameboard: ',gameboard_number)
    score = 0

    for num in board:
        if num not in numbers_drawn:
            score += num
        
    print('score: ', score * last_drawn_number)
                    


# offset: ignore first lines as we are only interested in the gameboards
def read_gameboards(filename, offset):
    # structure will be like this:
    # ###########################
    # h1 | h2 | h3 | ... | hn |  #
    # row_counter1 | ....| rcn|  #
    # col_counter1 | ....| ccn|  #
     ############################
    gameboards = []
    
    # read file
    file = open(filename)
    lines = file.readlines()

    # iterate over report
    for i in range(offset,len(lines),6):

        hn = {}

        # iterate over gameboard
        for j in range(0,5):
            trim_line_and_store_line(lines[i+j],hn,j)
        
        gameboards.append([hn, [0] * 5, [0] * 5])

    return gameboards



def trim_line_and_store_line(line,gameboard,line_num):
    line = line.rstrip().split()

    for column_num, number in enumerate(line):
        if number not in gameboard:
            gameboard[int(number)] = ([(line_num,column_num)])
        else:
            gameboard[int(number)].append((line_num,column_num))

def read_numbers_to_draw(filename):
    if filename == 'example_input.txt':
        numbers_to_draw = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    else:
        numbers_to_draw = [18,99,39,89,0,40,52,72,61,77,69,51,30,83,20,65,93,88,29,22,14,82,53,41,76,79,46,78,56,57,24,36,38,11,50,1,19,26,70,4,54,3,84,33,15,21,9,58,64,85,10,66,17,43,31,27,2,5,95,96,16,97,12,34,74,67,86,23,49,8,59,45,68,91,25,48,13,28,81,94,92,42,7,37,75,32,6,60,63,35,62,98,90,47,87,73,44,71,55,80]

    return numbers_to_draw

def main():
    print('advent_of_code: day four')
    print('-------------------------')

    # 1. read numbers_to_draw
    numbers_to_draw = read_numbers_to_draw('test_input.txt')

    # 2. store boards in 'appropriate' data structure
    # -------------------------------------------------
    # will use a two dimensional array of all gameboards with 3 rows and n gameboards
    #  row 1: contains hashmap of all numbers for the corresponding gameboard
    #  row 2: contains a list which remembers the numbers drawn of a row
    #  row 3: contains a list which remembers the columns drawn of a row
    gameboards = read_gameboards('test_input.txt', 2)

    # 3. compute game
    bingo(gameboards, numbers_to_draw)

if __name__ == '__main__':
    main()

