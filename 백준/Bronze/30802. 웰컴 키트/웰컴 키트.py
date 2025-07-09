import sys
input = sys.stdin.readline

n = int(input())

customer = list(map(int, input().split()))

shirt, pen = map(int, input().split())

pack = 0

for index in range(len(customer)):
    if customer[index] > shirt:
        if customer[index] % shirt > 0:
            pack += (customer[index] // shirt) + 1
        else:
            pack += customer[index] // shirt
    elif 0 < customer[index] <= shirt:
        pack += 1
print(pack)
print (n // pen, n % pen)