import numpy as np

def read_coordinates(filename):
    file = open(filename)
    coordinates = set()
    fold_instructions = []

    for line in file:
        line = line.replace('\n','')

        if 'fold' in line:
            fold_instructions.append(line)
        elif ',' in line:            
            line = line.split(',')
            coordinates.add((int(line[0]),int(line[1])))

    return coordinates, fold_instructions


def execute_fold(coordinates, fold_type):
    axis_to_fold = 0 # 0 represents x-axes
    axis_static = 1
    fold_index = int(fold_type.split('=')[1])
    coordinates_mirrored = set()

 
    if 'y' in fold_type:
        axis_to_fold = 1
        axis_static = 0

    for coord in coordinates:
        if coord[axis_to_fold] < fold_index:
            coordinates_mirrored.add(coord)
            continue

        # mirror original coordinate
        mirrored = fold_index - (coord[axis_to_fold] - fold_index)
        if axis_to_fold == 1:
            coord_mirrored = (coord[axis_static],mirrored)
        else:
            coord_mirrored = (mirrored, coord[axis_static])

        if coord_mirrored[axis_to_fold] >= 0 and coord_mirrored not in coordinates_mirrored:
            coordinates_mirrored.add(coord_mirrored)
            

    return coordinates_mirrored

def count_visible_dots(coordinates):
    print(len(coordinates))


def visualize_coordinates(coordinates, fold_num):
    max_x = 0
    max_y = 0
    for x,y in coordinates:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    max_x += 1
    max_y += 1
    matrix = [[' ' for x in range(max_x)] for y in range(max_y)] 

    for x,y in coordinates:
        matrix[y][x] = '#'

    
    m = np.matrix(matrix)

    filename = 'output/outfile' + str(fold_num) + '.txt'
    with open(filename,'w') as f:
        for line in matrix:
             f.write(' '.join([str(a) for a in line]) + '\n')
        
    print(m)


def main():
    print('advent_of_code: day thirteen')
    print('--------------------------')

    # read input
    coordinates, fold_instructions = read_coordinates('test_input.txt')

    #coordinates = execute_fold(coordinates,fold_instructions[0])

    #visualize_coordinates(coordinates, 100)

    #count_visible_dots(coordinates)

    for i,instruction in enumerate(fold_instructions):
        # execute fold
        coordinates = execute_fold(coordinates,instruction)

        # visualize coordinates
        visualize_coordinates(coordinates, i)

        # count dots
        count_visible_dots(coordinates)





if __name__ == "__main__":
    main()