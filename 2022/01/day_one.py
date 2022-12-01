def get_input_from_txt(filename):
    file = open(filename)
    report = []
    addup = False
    for line in file:
        if line.strip():
            if addup:
                report[-1] += int(line)
            else:
                report.append(int(line))
                addup = True
        else:
            addup = False 
    return report





def main():
    print('advent_of_code: day one')

    # read reports
    report_example = get_input_from_txt('example_input.txt')
    report_test = get_input_from_txt('test_input.txt')

    # compute part one
    print('part one')
    print(max(report_example))
    print(max(report_test))

    # compute part two
    print('part two')
    print(sum(sorted(report_example)[len(report_example)-3:]))
    print(sum(sorted(report_test)[len(report_test)-3:]))

if __name__ == "__main__":
    main()