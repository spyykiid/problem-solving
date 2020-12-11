from cmath import phase

z = complex(raw_input())

ph = phase(z)
ra = abs(z)

print str(ra)
print str(ph)
