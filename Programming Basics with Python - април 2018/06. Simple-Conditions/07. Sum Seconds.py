time1 = int(input())
time2 = int(input())
time3 = int(input())

total = time1 + time2 + time3


min = total // 60
sec = total % 60

if sec < 10:
    print(str(min) + ":0" + str(sec))
else:
    print(str(min) + ":" + str(sec))
