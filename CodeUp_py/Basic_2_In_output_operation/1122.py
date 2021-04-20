# CodeUp #1122

sec = list(map(int, input().split()))

minute = sec[0] / 60
rem_sec = sec[0] % 60

print('{} {}'.format(int(minute), rem_sec))