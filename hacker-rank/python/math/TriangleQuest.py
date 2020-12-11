for i in range(1, input()):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print i * sum(map(lambda x: 10**x, range(i)))
    # print  i * 10**i / 9
