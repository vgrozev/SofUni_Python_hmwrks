square_side_N = int(input())
tail_width_W = float(input())
tail_length_L = float(input())
bench_width_M = int(input())
bench_length_O = int(input())

total_area = pow(square_side_N, 2)
bench_area = bench_width_M * bench_length_O
area_to_cover = total_area - bench_area
tail_area = tail_width_W * tail_length_L
number_of_tails = area_to_cover / tail_area
time_needed = number_of_tails * 0.2

print("%.2f" % number_of_tails)
print("%.2f" % time_needed)

