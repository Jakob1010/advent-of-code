import collections

def read_polymer_template(filename):
    file = open(filename)
    polymer_mapper = {}
    polymer_template = ''

    for line in file:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        if len(line.split('->')) > 1:
            rule = line.split('->')
            polymer_mapper[rule[0]] = rule[1]
        elif line != '':
            polymer_template = line


    return polymer_mapper, polymer_template

def count_characters(polymer_template):
    pairs_counter = {}
    letter_counter = {}

    # count letters
    for c in polymer_template:
        if c in letter_counter:
            letter_counter[c] += 1
        else:
            letter_counter[c] = 1

    # count pairs
    for i in range(0,len(polymer_template)-1):
        pair = polymer_template[i]+polymer_template[i+1]

        if pair in pairs_counter:
            pairs_counter[pair] += 1
        else:
            pairs_counter[pair] = 1

    return pairs_counter, letter_counter

def insert_process(polymer_mapper, polymer_template, n):
    pairs_counter, letter_counter = count_characters(polymer_template)
    
    for i in range(0,n):
        temp = {}
        for pair, letter in polymer_mapper.items():
            if pair in pairs_counter:
                match_count = pairs_counter[pair]

                first_pair = pair[0] + letter
                second_pair = letter + pair[1]

                if letter in letter_counter:
                    letter_counter[letter] += match_count
                else:
                    letter_counter[letter] = match_count 
                    
                if first_pair in temp:
                    temp[first_pair] += match_count
                else:
                    temp[first_pair] = match_count
                
                if second_pair in temp:
                    temp[second_pair] += match_count
                else:
                    temp[second_pair] = match_count    

        pairs_counter = temp
                                     
    return letter_counter

def compute_most_and_least_frequent_character_sum(text):
    least_freq = float("inf")
    most_freq = -1

    for key, item in text.items():
        least_freq = min(item,least_freq)
        most_freq = max(item, most_freq)

    print('solution: ', most_freq - least_freq)

def main():
    print('advent_of_code: day fourteen')
    print('----------------------------')

    # read input
    polymer_mapper, polymer_template = read_polymer_template('test_input.txt')


    # insert characters 
    letter_freq = insert_process(polymer_mapper, polymer_template, 40)


    # compute solution part 1
    compute_most_and_least_frequent_character_sum(letter_freq)


if __name__ == "__main__":
    main()