n, k = input().split()
n = int(n)
k = int(k)


if n / 3 > k:
    a = n//3 - k + 1
    print(a)
else:
    print(0)