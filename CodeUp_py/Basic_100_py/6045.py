a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
add = a + b + c
avg = add/3
print(add, '%.2f'%avg, sep=' ')
# print(add, format(avg, ".2f"))