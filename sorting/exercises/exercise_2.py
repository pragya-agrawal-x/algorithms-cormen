def insertion_sort_descending(input_sequence):
    for i in xrange(1, len(input_sequence)):
        key = input_sequence[i]
        j = i - 1
        while j >= 0 and input_sequence[j] < key:
            input_sequence[j + 1] = input_sequence[j]
            j = j - 1
        input_sequence[j + 1] = key


def find_index(input_sequence, element):
    index = None
    for i in xrange(0, len(input_sequence)):
        if input_sequence[i] == element:
            index = i
            break
    return index