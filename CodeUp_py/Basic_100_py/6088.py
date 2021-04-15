# CodeUp #6088

def main():
    a, d, n = map(int, input().split())
    
    a = a + d*(n-1)
    print(a)

main()

''' 모범답안
a,d,n=input().split()

a=int(a)
d=int(d)
n=int(n)

s=a
for i in range(2, n+1):
   s+=d

print(s) '''