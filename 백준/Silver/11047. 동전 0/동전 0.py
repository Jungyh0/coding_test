n, k = map(int, input().split())

coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)
    
def greedy(money, coins):
    coins.sort(reverse=True)
    cnt = 0
    
    for coin in coins:
        num = money // coin
        cnt += num
        money %= coin
            
    return cnt

print(greedy(k, coins))