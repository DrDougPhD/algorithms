# Given a sequence of N numbers (A[1], A[2], ..., A[N]), find the length of
# the longest non-decreasing sequence.


def solve(sequence):
    solutions = initialize_solutions(sequence)

    for state, current_number in enumerate(sequence):
        # Find the lower states that can transition to the current state
        feasible_lower_states = {
            j for j, value in enumerate(sequence[:state])
            if value <= current_number
        }

        # Iterate over the lower states and see if adding the current number
        # to the lower state's sequence results in a longer sequence.
        for j in feasible_lower_states:
            if solutions[j] + 1 > solutions[state]:
                solutions[state] = solutions[j] + 1
                print('Better state found for state {}: {} numbers'.format(
                    state, solutions[state]
                ))

        print('')


# Initially, for each number in the sequence, a solution is to only include
# that number in the sequence. Thus, an initial solution would to be only
# include one number.
def initialize_solutions(sequence):
    return [1 for _ in sequence]


if __name__ == '__main__':
    solve(sequence=(5, 3, 4, 8, 6, 7))
