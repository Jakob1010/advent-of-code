import numpy as np

adjacent_octo = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

def read_input(filename):
    file = open(filename)
    dumbo_matrix = []

    for line in file:
        temp_matrix = []
        for num in line:
            if num != '\n':
                temp_matrix.append(int(num))
        dumbo_matrix.append(temp_matrix)

    return dumbo_matrix


def increase_by_one_all(dumbo_matrix):
    for i,line in enumerate(dumbo_matrix):
        for j, num in enumerate(line):
            dumbo_matrix[i][j]+=1


def increase_by_one_single(dumbo_matrix, i, j, overflow):  
    if (i < 0 or j < 0 or i >= len(dumbo_matrix) or j >= len(dumbo_matrix[0]) or (i,j) in overflow):   
        return

    dumbo_matrix[i][j] += 1
    if (dumbo_matrix[i][j] > 9) and (i,j) not in overflow:
        overflow.add((i,j))
        for r,c in adjacent_octo:
            increase_by_one_single(dumbo_matrix, i+r, j+c, overflow)
            

def check_overflows(dumbo_matrix):
    overflow = set()
    for i, row in enumerate(dumbo_matrix):
        for j, num in enumerate(row):
            if num == 10 and (i,j) not in overflow:
                dumbo_matrix[i][j] -= 1
                increase_by_one_single(dumbo_matrix, i, j, overflow)


def check_flashes_and_reset(dumbo_matrix):
    counter = 0
    for i, row in enumerate(dumbo_matrix):
        for j, num in enumerate(row):
            if num > 9:
                counter += 1
                dumbo_matrix[i][j] = 0

    return counter


def compute_flashes_naiv(dumbo_matrix):
    flashes = 0
    n = (len(dumbo_matrix)) * (len(dumbo_matrix[0]))
    print(n)
    first_simultaneously_flash = -1

    for step in range(1,500):
        increase_by_one_all(dumbo_matrix)
        check_overflows(dumbo_matrix)
        counter = check_flashes_and_reset(dumbo_matrix)

        if step <= 100:
            flashes += counter

        if (counter >= n and first_simultaneously_flash == -1):
            first_simultaneously_flash = step

        #print('step', step)
        #print(np.matrix(dumbo_matrix))

    print('solution part 1: ',flashes)  
    print('solution part 2: ',first_simultaneously_flash)  


def main():
    print('advent_of_code: day eleven')
    print('-------------------------')

    # read input
    dumbo_matrix = read_input('example_input.txt')

    # naiv implementation:
    compute_flashes_naiv(dumbo_matrix)


if __name__ == "__main__":
    main()