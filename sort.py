global a = input()
global b = input()
lcs(0, 0)
def lcs(pa, pb):
    if pa >= len(a):
	return 0
    if pb >= len(b):
	return 0
    if a[pa] == a[pb]:
	return 1 + lcs(pa + 1, pb + 1)
    x = lcs(pa +1, pb)
    y = lcs(pa, pb + 1)
    return max(x, y)


