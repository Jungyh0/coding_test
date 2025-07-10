n = input()
num_list= list(map(int, input().split()))

m = max(num_list)
s = sum(num_list)

print(s * 100 / m / int(n))