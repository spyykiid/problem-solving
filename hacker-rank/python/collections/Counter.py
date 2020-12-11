from collections import Counter

n_sizes = raw_input()
sizes_avail = raw_input().split()
size_counter = Counter(sizes_avail)
n_cust = int(raw_input())
sum_ = 0
for _ in range(n_cust):
    size, amount = raw_input().split()
    if size_counter[size] != 0:
        sum_ += int(amount)
        size_counter[size] = size_counter[size] - 1

print sum_
