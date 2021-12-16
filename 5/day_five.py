def read_lines(filename):
    lines = []
    file = open(filename)

    for line in file:
        numbers = line.split()
        start = numbers[0].split(',')
        end = numbers[2].split(',')

        # convert to int
        start[0] = int(start[0])
        start[1] = int(start[1])
        end[0] = int(end[0])
        end[1] = int(end[1])

        # only append vertical/horizontal lines
        if start[0] == end[0] or start[1] == end[1]:

            # append lines so that start point is 'smaller'
            if start[0] < end[0] or start[1] < end[1]:
                lines.append((start,end))
            else:
                lines.append((end,start))

    return lines


def draw_lines(lines):
    counter = 0
    points = {}

    for start, end in lines:
        
        x_or_y = 1
        if start[1] == end[1]:
            x_or_y = 0

        while start[x_or_y] != end[x_or_y]+1:

            if (start[0],start[1]) in points:
                points[(start[0],start[1])] += 1
            else:
                points[(start[0],start[1])] = 1

            if points[(start[0],start[1])] == 2:
                counter += 1

            start[x_or_y] += 1

    print(counter)


def main():
    print('advent_of_code: day five')
    print('-------------------------')

    # read lines
    lines = read_lines('test_input.txt')

    # draw lines
    draw_lines(lines)


if __name__=='__main__':
    main()