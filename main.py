import sys


def add_indices_last(raw):
    last_indices = []
    a = c = t = g = 0
    for char in raw:
        if char == 'A':
            new_char = (char, a)
            a += 1
        elif char == 'C':
            new_char = (char, c)
            c += 1
        elif char == 'T':
            new_char = (char, t)
            t += 1
        elif char == 'G':
            new_char = (char, g)
            g += 1
        else:
            new_char = ('$', 0)
        last_indices.append(new_char)
    return last_indices


def inverse_bwt(bwt):
    with_index = add_indices_last(bwt)
    first_line = sorted(with_index)
    inverse_key = dict()
    for i in range(len(with_index)):
        inverse_key[with_index[i]] = first_line[i]
    # print(inverse_key)
    inverse = str()
    cur_key = ('$', 0)
    while True:
        cur_key = inverse_key[cur_key]
        inverse += cur_key[0]
        if cur_key == ('$', 0):
            break
    return inverse


if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    file_input = inFile.readline()
    while file_input.endswith("\n"):
        file_input = file_input[:len(file_input)-1]
    inFile.close()
    answer = inverse_bwt(file_input)
    f = open("output.txt", "w")
    sys.stdout = f
    print(answer)
    f.close()
