from itertools import product

K, M = map(int, raw_input().split())

N = (map(int, raw_input().split())[1:] for _ in range(K))
# print type(N),list(N)
# print list(product(*N))
results = map(lambda x: sum(i**2 for i in x) % M, product(*N))
print(max(results))

#sum_ = 0
# for _ in range(k):
#  Ni = map(int, raw_input().split())[1:]
# print Ni
#  maxNi = max([ x**2 % M for x in Ni])
# print maxNi
#  sum_ += maxNi

# print sum_ % M
