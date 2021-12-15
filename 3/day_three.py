def read_file(file):
    report = []
    file = open(file)

    for line in file:
        line_list = []
        for number in line:
            if number != '\n':
                line_list.append(int(number))
        report.append(line_list)

    return report


def compute_epsilon_gamma(report):
    epsilon = ''
    gamma = ''
    columns = len(report[0])
    rows = len(report)

    for i in range(0,columns):
        counter = 0
        for j in range(0,rows):
            print(report[j][i])
            counter += report[j][i]
            if counter > rows / 2:
                gamma+='1'
                epsilon+='0'
                break
            elif j > rows / 2 and j-counter >= rows/2:
                gamma+='0'
                epsilon+='1'
                break

    print(epsilon,gamma)
    print((int(epsilon,2)*int(gamma,2)))


def main():
    # compute example
    report = read_file('example_input.txt')
    compute_epsilon_gamma(report)

    # compute test
    report2 = read_file('test_input.txt')
    compute_epsilon_gamma(report2)

if __name__ == "__main__":
    main()