# CodeUp #6092

def main():
    n = int(input())
    a = input().split()

    for i in range(len(a)):
        a[i]=int(a[i])

    d = []
    for i in range(24):
        d.append(0)
    for i in range(len(a)):
        d[a[i]] += 1
    for i in range(1, 24):
        print(d[i], end=' ')

main()