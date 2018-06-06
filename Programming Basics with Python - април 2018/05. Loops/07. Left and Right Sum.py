n = int(input())

left_sum = 0
right_sum = 0

for i in range(0, 2*n):
    if i < n:
        left_sum += int(input())
    else:
        right_sum += int(input())

if left_sum == right_sum:
    print("Yes, sum =", left_sum)
else:
    print("No, diff =", abs(left_sum - right_sum))
