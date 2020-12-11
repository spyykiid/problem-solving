from pythonds.basic.stack import Stack


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(128))


def baseConverter(decNumber,base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


print(baseConverter(25,8))
print(baseConverter(26,26))


