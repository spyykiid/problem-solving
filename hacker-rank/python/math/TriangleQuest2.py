for i in xrange(1, int(raw_input()) + 1):
    print (10**i / 9)**2
# Another Method 01:
for i in range(1, int(raw_input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2
# Another Method 02:
for i in range(1, int(raw_input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print [1, 121, 12321, 1234321, 123454321, 12345654321,
           1234567654321, 123456787654321, 12345678987654321][i - 1]
