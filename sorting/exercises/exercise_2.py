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

def find_smallest_element(input_sequence):
    temp = input_sequence[0]
    for i in xrange(1, len(input_sequence)):
        if input_sequence[i] < temp:
            temp = input_sequence[i-1]
    return temp