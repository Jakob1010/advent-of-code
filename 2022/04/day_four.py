import textwrap


def get_input_from_txt(filename):
    file = open(filename)
    report = []
    for line in file:
        if line.strip():
            line_clean = line.replace('\n', '')
            report.append(line_clean)
    return report

def get_priority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def ev_part_one(input):
    p = 0
    for line in input:
        f, s = line.split(',')
        elve1_start, elve1_end = f.split('-')
        elve2_start, elve2_end = s.split('-')
        elve1 = set()
        elve2 = set()
        #print(elve2_start, elve2_end)
        for i in range(int(elve1_start),int(elve1_end)+1):
            elve1.add(i)
        for i in range(int(elve2_start),int(elve2_end)+1):
            elve2.add(i)
        inter = elve1 & elve2
        if inter == elve1 or inter == elve2:
            p += 1
    return p

def ev_part_two(input):
    overlaps = 0
    for line in input:
        f, s = line.split(',')
        elve1_start, elve1_end = f.split('-')
        elve2_start, elve2_end = s.split('-')
        elve1 = set()

        print(f, s)
        for i in range(int(elve1_start),int(elve1_end)+1):
            elve1.add(i)
        for i in range(int(elve2_start),int(elve2_end)+1):
            if i in elve1:
                overlaps += 1
                break

    return overlaps


def main():
    print('advent_of_code: day one')

    # read reports
    report_example = get_input_from_txt('example_input.txt')
    report_test = get_input_from_txt('test_input.txt')

    # compute part one
    print('part one')
    print(ev_part_one(report_example))
    print(ev_part_one(report_test))

    # compute part two
    print('part two')
    print(ev_part_two(report_example))
    print(ev_part_two(report_test))

if __name__ == "__main__":
    main()