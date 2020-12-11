n, m = raw_input().split()
allele = raw_input().split()
setA = set(raw_input().split())
setB = set(raw_input().split())


happiness = sum([(e in setA) - (e in setB) for e in allele])

print happiness
