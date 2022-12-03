score_mapper_1 = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
    }


score_mapper_2 = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
    }


parentheses_mapper = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}


def read_code(filename):
    file = open(filename)
    chunk_lines = []

    for line in file: 
        chunk_lines.append(line.replace('\n','')) 

    return chunk_lines


def score_incomplete_lines(incomplete_lines):
    score_2 = []

    for line in incomplete_lines:
        score_temp = 0
        for opening_parenthesis in line[::-1]:
            closing_parenthesis = parentheses_mapper[opening_parenthesis]
            score_temp *= 5
            score_temp += score_mapper_2[closing_parenthesis]
        score_2.append(score_temp)

    score_2.sort()
    score_2 = score_2[len(score_2)//2]
    
    print('part 2 score: ',score_2)



def score_corrupted_chunks(chunk_lines):
    score_1 = 0
    incomplete_lines = []

    for line in chunk_lines: 
        score_1 += find_corrupted(line, incomplete_lines)

    print('part 1 score: ',score_1)
    return incomplete_lines


def find_corrupted(line,incomplete_lines):
    substr = ''

    for i in range(0,len(line)):

        p = line[i] # current parenthesis

        if p in parentheses_mapper: # opening parenth
            substr += p
        elif substr == '':
            return 0
        elif parentheses_mapper[substr[-1]] == p: # found matching parenth
            substr = substr[0:len(substr)-1]
        else:
            return score_mapper_1[p]

    incomplete_lines.append(substr) 
    return 0
    

def main():
    print('advent_of_code: day ten')
    print('-------------------------')

    # read input
    chunk_lines = read_code('test_input.txt')

    # compute score for part 1
    incomplete_lines = score_corrupted_chunks(chunk_lines)
    
    # compute score for part 2
    score_incomplete_lines(incomplete_lines)

if __name__ == "__main__":
    main()