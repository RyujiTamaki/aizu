def is_prime(n):
    i = 2

    while True:
        if i * i > n:
            break
        if n % i == 0:
            return False
        i += 1

    return n != 1


input_num = int(input())

ans = 0
for _ in range(input_num):
    if is_prime(int(input())):
        ans += 1

print(ans)
