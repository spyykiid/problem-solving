nEng = raw_input()
eng_roll = set(raw_input().split())
nFre = raw_input()
fre_roll = set(raw_input().split())

# Mutually exclusive and union is called symmetric difference.
eng_only = eng_roll ^ fre_roll
print len(eng_only)
