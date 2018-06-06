n = int(input())

sum_num = int(input())
max_num = sum_num

for i in range(1, n):
    next_num = int(input())
    sum_num += next_num

    if next_num > max_num:
        max_num = next_num

final_sum = sum_num - max_num
if final_sum == max_num:
    print("Yes Sum =", final_sum)
else:
    print("No Diff =", abs(final_sum - max_num))
