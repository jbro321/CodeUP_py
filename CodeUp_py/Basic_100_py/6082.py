# CodeUp #6082

n = int(input())
for i in range(1, n+1):
    if i%10==3:
        print("X", end=' ')
    elif i%10==6:
        print("X", end=' ')
    elif i%10==9:
        print("X", end=' ')
    else:
        print(i, end=' ')

''' 모범답안

 n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ') '''