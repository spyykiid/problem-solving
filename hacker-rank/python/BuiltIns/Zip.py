N, X = map(int, raw_input().split())
subs = []
for _ in range(X):
    subs.append(map(float, raw_input().split()))
zipp = zip(*subs)

for item in zipp:
    print round(sum(item) / X, 1)
