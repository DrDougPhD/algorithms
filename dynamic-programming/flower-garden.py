# https://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
# You are planting a flower garden with bulbs to give you joyous flowers
# throughout the year. However, you wish to plant the flowers such that they
# do not block other flowers while they are visible.
#
# You will be given a int[] height, a int[] bloom, and a int[] wilt. Each type
# of flower is represented by the element at the same index of height, bloom,
# and wilt. height represents how high each type of flower grows, bloom
# represents the morning that each type of flower springs from the ground,
# and wilt represents the evening that each type of flower shrivels up and
# dies. Each element in bloom and wilt will be a number between 1 and 365
# inclusive, and wilt[i] will always be greater than bloom[i]. You must plant
# all of the flowers of the same type in a single row for appearance, and you
# also want to have the tallest flowers as far forward as possible. However,
# if a flower type is taller than another type, and both types can be out of
# the ground at the same time, the shorter flower must be planted in front of
# the taller flower to prevent blocking. A flower blooms in the morning, and
# wilts in the evening, so even if one flower is blooming on the same day
# another flower is wilting, one can block the other.
#
# You should return a int[] which contains the elements of height in the order
# you should plant your flowers to acheive the above goals. The front of the
# garden is represented by the first element in your return value, and is
# where you view the garden from. The elements of height will all be unique,
# so there will always be a well-defined ordering.
#
# Constraints
# -	height will have between 2 and 50 elements, inclusive.
# -	bloom will have the same number of elements as height
# -	wilt will have the same number of elements as height
# -	height will have no repeated elements.
# -	Each element of height will be between 1 and 1000, inclusive.
# -	Each element of bloom will be between 1 and 365, inclusive.
# -	Each element of wilt will be between 1 and 365, inclusive.
# -	For each element i of bloom and wilt, wilt[i] will be greater than bloom[i].

from utils import heap


def solve(height, bloom, wilt):
    print('-' * 120)

    ordered_by_height = list(heap.sort(
        values=[
            (h, i)
            for i, h in enumerate(height)
        ],
        reverse=True,
        key=lambda x: x[0],
    ))
    # ordered_by_height = [
    #     (h, i)
    #     for i, h in enumerate(height)
    # ]
    # ordered_by_height.sort(key=lambda x: x[0], reverse=True)

    ordering = [ordered_by_height[0][0]]

    for index, (h, i) in enumerate(ordered_by_height[1:], 1):
        print('Processing flower with height {}'.format(h))
        print('Only need to consider: {}'.format(ordered_by_height[:index]))

        feasible_lower_states = [
            (height_j, j)
            for height_j, j in ordered_by_height[:index]
            if intervals_overlap(
                (bloom[i], wilt[i]),
                (bloom[j], wilt[j])
            )
        ]

        print('Feasible lower states: {}'.format(feasible_lower_states))

        if not feasible_lower_states:
            ordering.append(h)

        else:
            most_restrictive_height, j = min(feasible_lower_states,
                                             key=lambda x: x[0])
            index_of_most_restrictive = ordering.index(most_restrictive_height)
            ordering.insert(index_of_most_restrictive, h)

        print('Current ordering: {}'.format(ordering))
        print('')

    return ordering


def intervals_overlap(i, j):
    if i[0] > j[1]:
        return False
    if i[1] < j[0]:
        return False
    return True


if __name__ == '__main__':
    def list_equals(V, W):
        for v, w in zip(V, W):
            if v != w:
                return False
        return True

    assert list_equals(
        solve(
            height=(5,4,3,2,1),
            bloom=(1,1,1,1,1),
            wilt=(365,365,365,365,365),
        ),
        [1,  2,  3,  4,  5]
    )
    assert list_equals(
        solve(
            height=(5,4,3,2,1),
            bloom=(1,5,10,15,20),
            wilt=(4,9,14,19,24),
        ),
        [5,  4,  3,  2,  1]
    )
    assert list_equals(
        solve(
            height=(5, 4, 3, 2, 1),
            bloom=(1,5,10,15,20),
            wilt=(5,10,15,20,25),
        ),
        [1,  2,  3,  4,  5]
    )
    assert list_equals(
        solve(
            height=(5,4,3,2,1),
            bloom=(1,5,10,15,20),
            wilt=(5,10,14,20,25),
        ),
        [3,  4,  5,  1,  2]
    )
    assert list_equals(
        solve(
            height=(1,2,3,4,5,6),
            bloom=(1,3,1,3,1,3),
            wilt=(2,4,2,4,2,4),
        ),
        [2,  4,  6,  1,  3,  5]
    )
    assert list_equals(
        solve(
            height=(3,2,5,4),
            bloom=(1,2,11,10),
            wilt=(4,3,12,13),
        ),
        [4,  5,  2,  3]
    )
