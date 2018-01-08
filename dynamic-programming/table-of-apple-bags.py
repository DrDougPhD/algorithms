# A table composed of N x M bags, each having a certain quantity of apples,
# is given. You start from the upper-left corner. At each step you can go
# down or right one cell. Find the maximum number of apples you can collect.


def solve(table):
    M = len(table[0])
    if M == 0:
        return 0

    solutions = [
        list(row)
        for row in table
    ]

    for i, row in enumerate(table):
        for j, cell in enumerate(row):
            feasible_lower_states = []
            if i > 0:
                feasible_lower_states.append(solutions[i-1][j])
            if j > 0:
                feasible_lower_states.append(solutions[i][j-1])

            if not feasible_lower_states:
                continue

            solutions[i][j] = cell + max(feasible_lower_states)
            print('{} solution: {}'.format((i,j), solutions[i][j]))

    return solutions[-1][-1]


if __name__ == '__main__':
    assert solve(table=[[],]) == 0
    assert solve(table=[
        [5, 6, 2],
        [1, 3, 9]
    ]) == 23
