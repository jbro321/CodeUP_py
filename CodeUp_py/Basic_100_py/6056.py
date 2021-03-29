a, b = input().split()
a1 = bool(int(a))
b1 = bool(int(b))
print((a1 and (not b1)) or ((not a1) and b1))