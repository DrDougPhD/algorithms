# https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009
# The old song declares "Go ahead and hate your neighbor", and the residents of
# Onetinville have taken those words to heart. Every resident hates his next-
# door neighbors on both sides. Nobody is willing to live farther away from the
# town's well than his neighbors, so the town has been arranged in a big
# circle around the well. Unfortunately, the town's well is in disrepair and
# needs to be restored. You have been hired to collect donations for the
# Save Our Well fund.
#
# Each of the town's residents is willing to donate a certain amount,
# as specified in the int[] donations, which is listed in clockwise order
# around the well. However, nobody is willing to contribute to a fund to which
# his neighbor has also contributed. Next-door neighbors are always listed
# consecutively in donations, except that the first and last entries in
# donations are also for next-door neighbors. You must calculate and return the
# maximum amount of donations that can be collected.


def solve(donations):
    # Initialize data structures
    max_donations_of_counterclockwise_neighbors = list(donations)
    max_donations = max(donations)
    includes_first_resident = [False for _ in donations]
    includes_first_resident[0] = True

    if len(donations) <= 3:
        return max_donations

    for i, donation in enumerate(donations):
        is_last_resident = i + 1 == len(donations)

        is_not_counterclockwise_neighbor = lambda j: j < i-1
        is_not_clockwise_neighbor = lambda j: j != i+1 % len(donations)
        is_not_a_neighbor = lambda j: is_not_counterclockwise_neighbor(j) and\
                                      is_not_clockwise_neighbor(j)

        willing_neighbors = filter(is_not_a_neighbor, range(len(donations)))
        for j in willing_neighbors:
            donation_subtotal = max_donations_of_counterclockwise_neighbors[j]\
                              + donations[i]

            if is_last_resident and includes_first_resident[j]:
                donation_subtotal -= donations[0]

            if donation_subtotal \
                    > max_donations_of_counterclockwise_neighbors[i]:
                max_donations_of_counterclockwise_neighbors[i] \
                    = donation_subtotal

                max_donations = max(max_donations, donation_subtotal)
                includes_first_resident[i] = includes_first_resident[j]

    return max_donations


if __name__ == '__main__':
    assert solve(donations=(
        10, 3, 2, 5, 7, 8
    )) == 19
    assert solve(donations=(
        11, 15
    )) == 15
    assert solve(donations=(
        7, 7, 7, 7, 7, 7, 7
    )) == 21
    assert solve(donations=(
        1, 2, 3, 4, 5, 1, 2, 3, 4, 5
    )) == 16
    assert solve(donations=(
        94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
        6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
        52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72
    )) == 2926
