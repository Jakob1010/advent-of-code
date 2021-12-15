


def get_input_from_txt(filename):
    file = open(filename)
    report = []
    for line in file:
        report.append(int(line))
    return report

def print_number_of_increases(report):
    counter = 0

    for i, number in enumerate(report[1:]):
        if number > report[i]:
            counter += 1

    print(counter)

def main():
    print('advent_of_code: day one')

    # read reports
    report_example = get_input_from_txt('example_input.txt')
    report_test = get_input_from_txt('test_input.txt')

    # compute increases
    print_number_of_increases(report_example)
    print_number_of_increases(report_test)

if __name__ == "__main__":
    main()