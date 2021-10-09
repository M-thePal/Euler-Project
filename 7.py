def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = 1
i = 2

while n != 10002:
    if prime(i):
        n += 1
    i += 1
print(i-1)
