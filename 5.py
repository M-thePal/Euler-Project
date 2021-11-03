def facs(n):
    out = {}
    i = 2
    while n != 1:
        if n % i == 0:
            n /= i
            out[i] = (out[i]+1) if i in out else 1
        else:
            i += 1
    return out


def gen(n):
    out = {}
    for i in range(2, n+1):
        x = facs(i)
        for fac in x:
            out[fac] = max(out[fac], x[fac]) if fac in out else x[fac]
    o = 1
    for i in out:
        o *= (i**out[i])
    return o


print(gen(20))
