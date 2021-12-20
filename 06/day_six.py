def read_init_state(filename):
    file = open(filename)
    inital_state = []

    for line in file:
        nums = line.split(',')
        if len(nums) == 0:
            break
        inital_state.extend(map(int,nums))

    return inital_state


def compute_state_naiv(state, days):
    
    for day in range(0,days):
        for i in range(0,len(state)):
            state[i] -= 1
            if state[i] < 0:
                state[i] = 6
                state.append(8)

    print(len(state))


def compute_state_in_big_o_n(state, days):
    print('too lazy to implement')
    # iterate over init state
    # compute for all entries state[n]/days and append result to state
    # for entreis that are appended from init state we must compute state[n] / (days-days_of_init_state_fish)
    

def main():
    print('advent_of_code: day six')
    print('-------------------------')

    # get initial state
    initial_state = read_init_state("test_input.txt")

    # compute state after 80 days
    compute_state_naiv(initial_state, 80)
    

if __name__ == "__main__":
    main()