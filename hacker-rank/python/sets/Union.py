nEng = raw_input()
eng_roll = set(raw_input().split())
nFre = raw_input()
fre_roll = set(raw_input().split())

eng_fre_roll = eng_roll.union(fre_roll)
print len(eng_fre_roll)
