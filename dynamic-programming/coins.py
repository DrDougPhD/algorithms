# Given a list of N coins, their values (V1, V2, … , VN), and the total sum S,
# find the minimum number of coins the sum of which is S (we can use as many
# coins of one type as we want), or report that it’s not possible to select
# coins in such a way that they sum up to S.

def solve_1(coins, total_sum):
    solutions = initialize_solutions(total_sum)

    for smaller_sum in range(1, total_sum+1):
        # Build a set of coins that have a smaller or equal value of the
        # current sum.
        feasible_coins = {
            coin for coin in coins
            if coin <= smaller_sum
        }

        # Iterate over the set of feasible coins
        for coin in feasible_coins:
            previous_solution = solutions[smaller_sum-coin]
            if previous_solution < solutions[smaller_sum]:
                solutions[smaller_sum] = previous_solution + 1

    summarize_solutions(solutions)


def summarize_solutions(solutions):
    for smaller_sum in range(1, len(solutions)):
        print('Number of coins adding up to {: >3}: {} coins'.format(
            smaller_sum, solutions[smaller_sum]
        ))


def initialize_solutions(total_sum):
    # Initialize solutions table to indicate that no solutions have been
    # found for all states.
    solutions = []
    for i in range(total_sum + 1):
        solutions.append(float('inf'))

    # For the initial state of a sum 0, the optimal solution is 0 coins
    solutions[0] = 0
    return solutions


def solve(coins, total_sum):
    solutions = initialize_solutions(total_sum)

    for coin in coins:
        for i, solution_i in enumerate(solutions):
            if i+coin >= len(solutions):
                continue

            if solution_i + 1 < solutions[i+coin]:
                solutions[i + coin] = solution_i + 1

    summarize_solutions(solutions)


if __name__ == '__main__':
    solve(coins={1, 3, 5}, total_sum=11)
