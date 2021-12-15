
def get_input_from_txt(filename):
    file = open(filename)
    report = []
    for line in file:
        report.append(int(line))
    return report


def print_number_of_increases(report):
    counter = 0

    # compare window A with window B
    # exmaple: [1,2,3,4]
    # window A: [1,2,3]
    # window B: [2,3,4]
    for i, current in enumerate(report[3:]):
        # last_two: [2,3]
        last_two = report[i+1] + report[i+2]

        # window B > window A
        if last_two + current > last_two + report[i]:
            counter += 1

    print(counter)


def main():
    print('advent_of_code: day one')

    # read reports (same as in 1)
    report_example = get_input_from_txt('../1/example_input.txt')
    report_test = get_input_from_txt('../1/test_input.txt')

    # compute increases
    print_number_of_increases(report_example)
    print_number_of_increases(report_test)

if __name__ == "__main__":
    main()