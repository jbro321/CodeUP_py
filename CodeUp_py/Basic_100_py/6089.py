# CodeUp #6089

def main():
    a, r, n = map(int, input().split())
    
    a = a*r**(n-1)
    print(a)

main()

''' 모범답안
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a*r

print(a) '''