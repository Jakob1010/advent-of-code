def read_input(filename):
    file = open(filename)
    positions = []

    for line in file:
        nums = line.split(',')

        # no numbers found
        if len(nums)<= 1:
            break

        positions.extend(nums)

    return list(map(int, positions))


def determine_horizontal_pos(positions):
    positions = sorted(positions)
    median = positions[len(positions)//2]

    costs = 0

    for pos in positions:
        costs += abs(pos-median)
    
    print('total costs: ', costs)


def main():
    print('advent_of_code: day seven')
    print('-------------------------')

    # read input
    positions = read_input('test_input.txt')

    # compute 
    determine_horizontal_pos(positions)


if __name__ == "__main__":
    main()