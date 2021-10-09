seq = [0, 1]
while seq[-1]+seq[-2] < 4*(10**6):
    seq.append(seq[-1]+seq[-2])
sum = 0
for i in seq:
    if i % 2 == 0:
        sum += i
print(sum)
