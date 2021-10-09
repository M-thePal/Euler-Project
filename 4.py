start = 100
end = 999
out = []
for i in range(start, end+1):
    a1 = a2 = start
    while a2 != end+1:
        out.append(a1*a2)
        a2 += 1
    start += 1
out.sort(reverse=True)
for i in out:
    if str(i) == str(i)[::-1]:
        print(i)
        break
