# CodeUp #6096

def main():

    d = [[]*19 for _ in range(19)]
    for i in range(19):
        d[i]=list(map(int,input().split()))
    
    n = int(input())
    
    for i in range(n):
        x,y=map(int,input().split())
        
        for j in range(1, 20):
            if(d[x][j]==1):
                d[x][j]=0
            else: d[x][j]=1
        
        for j in range(1, 20):
            if(d[j][y]==1):
                d[j][y]=0
            else: d[j][y]=1
    
    for i in range(19):
        for j in range(19):
            print(d[i][j],end=' ')
        print()
    
main()

''' d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  for j in range(1, 20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print() '''