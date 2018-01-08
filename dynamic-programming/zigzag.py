# https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
# A sequence of numbers is called a zig-zag sequence if the differences
# between successive numbers strictly alternate between positive and negative.
# The first difference (if one exists) may be either positive or negative.
# A sequence with fewer than two elements is trivially a zig-zag sequence.

# For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences
# (6,-3, 5, -7, 3) are alternately positive and negative.
# In contrast, 1, 4, 7, 2, 5 and 1,7,4,5,5 are not zig-zag sequences, the first
# because its first two differences are positive and the second because its
# last difference is zero.

# Given a sequence of integers, sequence, return the length of the longest
# subsequence of sequence that is a zig-zag sequence.
# A subsequence is obtained by deleting some number of elements (possibly zero)
# from the original sequence, leaving the remaining elements in their original
# order.

def solve(sequence):
    if len(sequence) == 1:
        return 1

    zigzag_lengths   = [ 2  for _ in sequence]
    zigzag_diffs     = [ 0  for _ in sequence]
    zigzag_sequences = [[v] for v in sequence]

    max_zigzag_length = 2
    for i in range(1, len(sequence)):
        print('Zigzag subsequence ending at state {}'.format(i))

        zigzag_diffs[i] = sequence[i-1] - sequence[i]
        zigzag_sequences[i] = [sequence[i-1], sequence[i]]

        viable_lower_states = [
            j for j in range(i)
            if (zigzag_diffs[j] > 0 and sequence[j]-sequence[i] < 0)
            or (zigzag_diffs[j] < 0 and sequence[j]-sequence[i] > 0)
        ]

        for j in viable_lower_states:
            if zigzag_lengths[j] + 1 > zigzag_lengths[i]:
                zigzag_lengths[i] = zigzag_lengths[j] + 1
                zigzag_diffs[i] = sequence[j]-sequence[i]
                zigzag_sequences[i] = [*zigzag_sequences[j], sequence[i]]

                print('\tLonger subsequence for {} to {}:'
                      ' {} length'.format(j, i, zigzag_lengths[i]))
                print('\t{}'.format(tuple(zigzag_sequences[i])))

            max_zigzag_length = max(zigzag_lengths[i], max_zigzag_length)

        print('')

    print('Max zigzag sequence of length {}'.format(max_zigzag_length))
    return max_zigzag_length


if __name__ == '__main__':
    assert solve(sequence=(1, 7, 4, 9, 2, 5)) == 6
    assert solve(sequence=(1, 17, 5, 10, 13, 15, 10, 5, 16, 8)) == 7
    assert solve(sequence=(44,)) == 1
    assert solve(sequence=(1, 2, 3, 4, 5, 6, 7, 8, 9)) == 2
    assert solve(sequence=(
        374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
        600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
        67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
        477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
        249, 22, 176, 279, 23, 22, 617, 462, 459, 244
    )) == 36
    assert solve(sequence=(
        70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7,
        5, 5, 5, 1000, 32, 32
    )) == 8
