def find_basins(heatmap, lowest_points):
    basins = []

    for row,col in lowest_points:
        basin = {}
        basin[(row,col)] = heatmap[row][col]
        explore_basin(heatmap,row,col,basin)
        basins.append(basin)

    return basins


def explore_basin(heatmap, row, col, basin):
    num = heatmap[row][col]

    for (r,c) in [(1,0),(0,1),(-1,0),(0,-1)]: 
        neighbor = heatmap[row+r][col+c]
        if (row+r,col+c) not in basin and neighbor > num and neighbor not in [9, 10]:
            basin[(row+r,col+c)]=neighbor
            explore_basin(heatmap, row+r, col+c, basin)


def product_of_basins(basins):
    basins.sort(key=len,reverse=True)
    basins_length = 1

    for basin in basins[0:3]:
        basins_length *= len(basin)

    print('solution part 2: ', basins_length)


def find_lowest_points(heatmap):
    local_mins = []

    for row,line in enumerate(heatmap):
        for col, num in enumerate(line):
            if num != 10:
                check_local_min(row,col,num,local_mins,heatmap)
    
    return local_mins


def check_local_min(row, col, num, local_mins, heatmap):
    counter = 0

    for (r,c) in [(1,0),(0,1),(-1,0),(0,-1)]:
        if num < heatmap[row+r][col+c]:
            counter += 1

    if counter == 4:
        local_mins.append((row,col)) # append coordinates of local min


def sum_of_points(heatmap, lowest_points):
    risk_level = 0

    for r,c in lowest_points:
        risk_level += heatmap[r][c]

    # result is the sum of all local mins increased by one (=length of all local mins)
    print('solution part 1: ', risk_level + len(lowest_points))


def read_heatmap(filename):
    file = open(filename)
    # heatmap will store all numbers with an additional row/column of height 10
    heatmap = []

    for line in file:
        temp = []
        temp.append(10)
        for num in line:
            if num!='\n':
                temp.append(int(num))
        temp.append(10)
        heatmap.append(temp)

    # insert row of points with height=10 at the beginning and end of heatmap
    row_height_10 = [10] * len(heatmap[0])
    heatmap.insert(0,row_height_10)
    heatmap.append(row_height_10)

    return heatmap


def main():
    print('advent_of_code: day nine')
    print('-------------------------')

    # read file
    heatmap = read_heatmap('test_input.txt')

    # find coordinates of lowest points
    lowest_points = find_lowest_points(heatmap)

    # compute solution for part 1
    sum_of_points(heatmap, lowest_points)

    # find basins
    basins = find_basins(heatmap, lowest_points)

    # compute solutin for part 2
    product_of_basins(basins)

if __name__=='__main__':
    main()