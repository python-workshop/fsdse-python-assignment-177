def paren(n):
    ps = set(['(' * n + ')' * n])
    for i in range(1, n):
        for a in paren(i):
            for b in paren(n-i):
                ps.add(a + b)
    return ps

print(paren(3))