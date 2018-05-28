type_movie = input()
num_raws = int(input())
num_coluns = int(input())
total_gain = 0.0

if type_movie == "Premiere":
    total_gain = num_coluns * num_raws * 12.00
elif type_movie == "Normal":
    total_gain = num_coluns * num_raws * 7.50
else:
    total_gain = num_coluns * num_raws * 5

print("{:.2f}".format(total_gain))
