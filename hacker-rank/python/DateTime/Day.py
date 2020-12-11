import calendar

month, day, year = map(int, raw_input().split())

c = calendar.weekday(year, month, day)

if c == 0:
    print "MONDAY"
elif c == 1:
    print "TUESDAY"
elif c == 2:
    print "WEDNESDAY"
elif c == 3:
    print "THURSDAY"
elif c == 4:
    print "FRIDAY"
elif c == 5:
    print "SATURDAY"
elif c == 6:
    print "SUNDAY"
