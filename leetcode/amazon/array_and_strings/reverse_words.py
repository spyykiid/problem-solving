def reverseWords(str):
    """
    :type str: List[str]
    :rtype: void Do not return anything, modify str in-place instead.
    """
    '''Python way of reversing words'''
    # str = "".join(str)
    # str = str.split(" ")
    # start = 0
    # end = len(str) - 1
    # while start < end:
    #     str[start], str[end] = str[end], str[start]
    #     print(str)
    #     start += 1
    #     end -= 1
    # str = " ".join(str)




def main():
    reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])


if __name__ == '__main__':
    main()
