import textwrap


def get_input_from_txt(filename):
    file = open(filename)
    report = []
    for line in file:
        if line.strip():
            report.append(line[:-1])
    return report

def get_priority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def ev_part_one(input):
    p = 0
    for line in input:
        n = len(line)
        f, s = set(line[:n//2]), set(line[n//2:])
        dupl = f & s
        #print(dupl)
        for c in dupl:
            p += get_priority(c)

    return p

def ev_part_two(input):
    p = 0

    for i in range(0,len(input),3):
        f, s, t = set(input[i]), set(input[i+1]), set(input[i+2])
        dupl = f & s & t
        for c in dupl:
            p += get_priority(c)
    return p


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