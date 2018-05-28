n = int(input())
fUpper = input().upper()
lower = input().lower()
sUpper = input().upper()
m = int(input())
count = int(input()) +1

if n%10 > 2:
    n = 12 + (n//10)*10
else:
    n = 2 + (n//10)*10

if m%10 >= 5:
    m = 5 + (m//10)*10
else:
    m = (m//10)*10 -5
tmpn = 0
tmpfup = ""
tmplow = ""
tmpsup = ""
tmpm = 0

for x in range(n, 93, 10):
    for y in range(ord(fUpper), 91):
        for z in range(ord(lower), 123):
            for a in range(ord(sUpper), 91):
                for b in range(m, 14, -10):
                    if count == 0:
                        tmpm = b
                        break
                    else:
                        if not tmpm == b:
                            count -= 1
                        else:
                            break
                        tmpm = b
                if count == 0:
                    tmpsup = chr(a)
                    break
                else:
                    if not tmpsup == chr(a):
                        count -= 1
                    else:
                        break
                    tmpsup = chr(a)

            if count == 0:
                tmplow = chr(z)
                break
            else:
                if not tmplow == chr(z):
                    count -= 1
                else:
                    break
                tmplow = chr(z)

        if count == 0:
            tmpfup = chr(y)
            break
        else:
            if not tmpfup == chr(y):
                count -= 1
            else:
                break
            tmpfup = chr(y)

    if count == 0:
        tmpn = x
        break
    else:
        if not tmpn == x:
            count -= 1
        else:
            break
        tmpn = x
print(str(tmpn) + tmpfup + tmplow + tmpsup + str(tmpm))