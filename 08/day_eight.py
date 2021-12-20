def read_input(filename):
    file = open(filename)
    input = []

    for line in file:
        line_split = line.split('|')[1].split()
        input.append(line_split)

    return input


def translate_to_digits(letters):
    # 1, 4, 7, and 8 each use a unique number of segments
    translater_map = {
        2:1,
        4:4,
        3:7,
        7:8
    }
    unique_numbers = [2,4,3,7]
    counter = 0

    for letter_line in letters:
        for letter_combination in letter_line:
            if len(letter_combination) in unique_numbers:
                counter += 1
        
    print('Solution is:',counter)

def main():
    print('advent_of_code: day eight')
    print('-------------------------')

    # read file input
    input_file = read_input('test_input.txt')


    # translate to digits
    translate_to_digits(input_file)

if __name__ == "__main__":
    main()