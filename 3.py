i = 2
n = 600851475143
while n != 1:
    if n % i == 0:
        n /= i
    else:
        i += 1
print(i)
