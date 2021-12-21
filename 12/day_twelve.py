def read_map(filename):
    file = open(filename)
    cave_map = {}

    for line in file:
        line = line.replace('\n','')
        line = line.split('-')

        start = line[0]
        end = line[1]

        if start != 'start' and end != 'end':
            if start not in cave_map:
                cave_map[start] = [end]
            else:
                cave_map[start].append(end)

            if end not in cave_map:
                cave_map[end] = [start]
            else:
                cave_map[end].append(start)
        else:
            if start not in cave_map:
                cave_map[start] = [end]
            elif end != 'start':
                cave_map[start].append(end)

    return cave_map


def find_distinct_ways(cave_map):
    number_of_ways = 0
    start_points = cave_map['start']
    paths = []

    del cave_map['start']

    for cave in start_points:
        number_of_ways += visit_cave(cave_map, cave,0,'start',paths, False)
    
    #print(paths)
    print('distinct ways: ', number_of_ways)


def visit_cave(cave_map, cave, counter, visited, paths, double_visit):
    visited += ',' + cave
    counter = 0

    if cave == 'end':
        paths.append(visited)
        return 1

    if cave not in cave_map:
        return 0

    for c in cave_map[cave]:    
        if not c.islower() or c not in visited: #or not double_visit:
            #if c.islower() and c in visited:
            #    double_visit = True
            counter += visit_cave(cave_map, c, 0, visited, paths, double_visit)
            
            
    return counter



def main():
    print('advent_of_code: day twelve')
    print('--------------------------')

    # read input
    cave_map = read_map('example_input_small.txt')

    # compute number of distinct ways
    find_distinct_ways(cave_map)

if __name__ == "__main__":
    main()