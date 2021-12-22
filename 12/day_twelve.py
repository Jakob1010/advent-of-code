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
    start_points = cave_map['start']
    paths = []

    del cave_map['start']

    for cave in start_points:
        visit_cave(cave_map, cave,'start',paths, False)
    
    #print(paths)
    print('distinct ways: ', len(paths))


def visit_cave(cave_map, cave, visited, paths, double_visit):
    visited += ',' + cave

    if cave == 'end':
        paths.append(visited)
    elif cave not in cave_map:
        return 0
    else:
        for c in cave_map[cave]:    
            if not c.islower() or c not in visited or not double_visit:
                if c.islower() and c in visited:
                    double_visit = True
                    visit_cave(cave_map, c, visited, paths, double_visit)
                    double_visit = False
                else:
                    visit_cave(cave_map, c, visited, paths, double_visit)


def main():
    print('advent_of_code: day twelve')
    print('--------------------------')

    # read input
    cave_map = read_map('test_input.txt')

    # compute number of distinct ways
    find_distinct_ways(cave_map)

if __name__ == "__main__":
    main()