__author__ = 'Rahul Ponnada'


#num_list = [0, 1, 2, 3, 6, 14, 13, 12, 8, 0, 3, 11, 12, 56]
num_list = [15,14,12,0, 1, 2, 3, 6, 14, 13, 12, 8, 0, 3, 11, 12, 56]
#num_list = [10,9,8,7,6,5,4]
#num_list = [0, 1, 2, 3, 6, 14, 17]

def unimodal_seq():
    max_count = 0
    i_seq = 0
    i = 0
    d = 0
    c = 0
    while i < 16:
        if num_list[i+1] > num_list[i] and d == 0:
            c += 1
            i += 1
        elif num_list[i+1] < num_list[i]:
            d += 1
            i += 1
        else:
            if c+d+1 > max_count:
                max_count = c+d + 1
                j_seq = i
                i_seq = i - (c+d)

            c = d = 0

    if c+d+1 > max_count:
        max_count = c + d + 1
        i_seq = i - (c+d)
        j_seq = i
    return max_count


if __name__ == "__main__":
    print unimodal_seq()

