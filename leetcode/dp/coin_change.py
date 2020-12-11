import time 

coins = [1,2,5]
coins_mem = {} 

def cc(amount):
  # top down approach, recursion
  if amount <= 0:
    return 0
  
  if amount in coins_mem:
    return coins_mem.get(amount)

  c0 = cc(amount - coins[0]) + 1
  c1 = cc(amount - coins[1]) + 1
  c2 = cc(amount - coins[2]) + 1

  if not amount in coins_mem:
    coins_mem[amount] = min(c0, c1, c2)

  return min(c0, c1, c2)


def coin_change_bottom_up(amount):
  coins_mem = [amount+1] * (amount+1)
  coins_mem[0] = 0

  for i in range(1, amount+1):
    for j in coins:
      # print(i, j, coins_mem[i-j], coins_mem[i])
      if j <= i and coins_mem[i -j] + 1 < coins_mem[i]:
        coins_mem[i] = coins_mem[i-j] +1
  
  # print(coins_mem)
  return coins_mem[amount]

amount = 21
tic = time.perf_counter() #start time
print(cc(amount)) #top down approach
toc = time.perf_counter()
print(f'{toc - tic:0.10f} secs')

tic = time.perf_counter()
print(coin_change_bottom_up(amount)) #bottom up approach
toc = time.perf_counter()

print(f'{toc - tic:0.10f} secs')

