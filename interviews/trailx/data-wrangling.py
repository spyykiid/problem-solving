import sys
from collections import OrderedDict


def find_unique_names():
    num_lines = int(sys.stdin.readline().strip())
    uniq_name = OrderedDict()

    for line in sys.stdin:

        name, aadhar = line.split(':')
        aadhar = aadhar.strip()

        fullName = name
        if ',' in name:
            lastName, firstName = name.split(',')
            lastName = lastName.strip()
            firstName = firstName.strip()
            fullName = firstName + ' ' + lastName

        if uniq_name.get(aadhar) is None:
            uniq_name[aadhar] = fullName
        else:
            fullName = firstName + ' ' + lastName
            if len(fullName) > len(uniq_name.get(aadhar)):
                uniq_name[aadhar] = fullName

    for key, item in uniq_name.items():
        print(item + ":" + key)