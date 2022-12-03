# x = stein
# y = papier
# z = schere

def translate_opponent(o):
    if o == 'A':
        return 'X'
    elif o == 'B':
        return 'Y'
    elif o == 'C':
        return 'Z'

def get_winning_shape(shape):
     if shape == 'X':
        return 'Y'
     elif shape == 'Y':
        return 'Z'
     elif shape == 'Z':
        return 'X'   

def get_loser_shape(shape):
     if shape == 'X':
        return 'Z'
     elif shape == 'Y':
        return 'X'
     elif shape == 'Z':
        return 'Y'     


def get_input_from_txt(filename):
    file = open(filename)
    report = []
    for line in file:
        if line.strip():
            report.append(line)
    return report

def get_shape_score(shape):
    if shape == 'X':
        return 1
    elif shape == 'Y':
        return 2
    elif shape == 'Z':
        return 3

def get_game_score(x, y):
    if y == 'X' and x == 'Z':
        return 6
    elif y == 'Y' and x == 'X':
        return 6
    elif y == 'Z' and x == 'Y':
        return 6
    elif y == x:
        return 3
    else:
        return 0

def evaluate(report):
    score = 0
    for line in report:
        x, y  = line.split()
        x = translate_opponent(x)
        score += get_game_score(x,y)
        score += get_shape_score(y)
    return score

def evaluate_part_two(report):
    score = 0
    for line in report:
        x, y = line.split()
        x = translate_opponent(x)
        #print(x, y)
        if y == 'X':
            y = get_loser_shape(x)
        elif y == 'Z':
            y = get_winning_shape(x)
            score += 6
        else:
            y = x
            score += 3
        score += get_shape_score(y)
    return score





def main():
    print('advent_of_code: day two')

    # read reports
    report_example = get_input_from_txt('example_input.txt')
    report_test = get_input_from_txt('test_input.txt')

    # compute part one
    print('part one')
    print(evaluate(report_example))
    print(evaluate(report_test))

    print('part two')
    print(evaluate_part_two(report_example))
    print(evaluate_part_two(report_test))

if __name__ == "__main__":
    main()