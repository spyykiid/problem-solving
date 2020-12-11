N = int(raw_input())
N_list = set(map(int, raw_input().split()))

M = int(raw_input())
M_list = set(map(int, raw_input().split()))

N_diff = N_list.difference(M_list)
M_diff = M_list.difference(N_list)
symm_diff = sorted(N_diff.union(M_diff))

print "\n".join(map(str, symm_diff))
