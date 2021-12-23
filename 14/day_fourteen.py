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


def insert_process(polymer_mapper, polymer_template, n):
    template = polymer_template
    templates = []

    for i in range(0,n):
        temp = ''
        for i in range(0,len(template)-1):
            pair = template[i] + template[i+1]
            insert = ''
            if pair in polymer_mapper:
                insert = polymer_mapper[pair]
            temp += pair[0] + insert 

        temp += template[-1] # add last character
        template = temp
        temp = ''
        templates.append(template)

    return templates

def compute_most_and_least_frequent_character_sum(text):
    text_freq = collections.Counter(text)
    least_freq = 1000
    most_freq = -1

    for key, item in text_freq.items():
        least_freq = min(item,least_freq)
        most_freq = max(item, most_freq)

    print('solution part 1: ', most_freq - least_freq)

def main():
    print('advent_of_code: day fourteen')
    print('----------------------------')

    # read input
    polymer_mapper, polymer_template = read_polymer_template('test_input.txt')


    # insert characters 
    templates = insert_process(polymer_mapper, polymer_template, 10)


    # compute solution part 1
    compute_most_and_least_frequent_character_sum(templates[-1])


if __name__ == "__main__":
    main()