__author__ = 'Rahul Ponnada'

num_list = [0, 8, 4, 0, 2, 18, 15, 14, 15, 16, 8, 0, 3, 11, 12, 56]
#num_list = [0, 4, 6, 9, 13, 15, 10]

def long_subseq():
    i = 0
    j = 0
    length = 1
    loop_index = 0
    while loop_index < 15:
        if num_list[loop_index] <= num_list[loop_index+1]:
            ''' Increment the length by 1 if sequence is non-decreasing  '''
            length += 1
        else:
            ''' Get i and j if non-decreasing sequence next element is decreasing '''
            if (j-i)+1 <= length:
                j = loop_index
                i = abs((j+1)-length)
            length = 1
        loop_index += 1

    # Get i and j if longest sub sequence is on the end of the list
    if (j-i)+1 <= length:
        j = loop_index
        i = abs((j+1)-length)

    print "Longest sub sequence is from %d to %d"%(i, j)


if __name__ == "__main__":
    long_subseq()
