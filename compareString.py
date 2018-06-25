cache = {}
def compare(a, b, pa, pb):
    if pa >= len(a):
        return 0
    if pb >= len(b):
        return 0
    if a[pa] == b[pb]:
        return 1 + compare(a, b, pa + 1, pb + 1)

    x = compare(a, b, pa + 1, pb)
    y = compare(a, b, pa, pb + 1)
    return max(x, y)

for _ in range(4):
    a = input()
    b = input()
    print(compare(a, b, 0, 0))
