def merge_the_tools(string, k):
    string_split = [string[i: i + k] for i in range(0, len(string), k)]
    for st in string_split:
        merge = ''
        for s in st:
            if s not in merge:
                merge += s
        print merge


if __name__ == '__main__':
    # string, k = raw_input(), int(raw_input())
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)
