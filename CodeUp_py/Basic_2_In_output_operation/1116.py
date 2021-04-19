# CodeUp #1116

a, b = map(int, input().split())
print('%d+%d=%d' %(a, b, a+b))
print('%d-%d=%d' %(a, b, a-b))
print('%d*%d=%d' %(a, b, a*b))
print('%d/%d=%d' %(a, b, a/b))

print('{}+{}={}'.format(a, b, a+b))
print('{2}-{1}={0}'.format(a-b, b, a))
print('{}*{}={}'.format(a, b, a*b))
print('{}/{}={}'.format(a, b, int(a/b)))