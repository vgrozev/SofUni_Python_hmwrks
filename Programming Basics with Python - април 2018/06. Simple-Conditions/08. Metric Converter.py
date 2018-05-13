num = float(input())
from_metric = input()
to_metric = input()

# 1. convert all to meters

if from_metric == 'm':
    in_meters = num / 1
elif from_metric == 'mm':
    in_meters = num / 1000
elif from_metric == 'cm':
    in_meters = num / 100
elif from_metric =='mi':
    in_meters = num / 0.000621371192
elif from_metric == 'in':
    in_meters = num / 39.3700787
elif from_metric == 'km':
    in_meters = num / 0.001
elif from_metric == 'ft':
    in_meters = num / 3.2808399
elif from_metric == 'yd':
    in_meters = num / 1.0936133

# 2. from meters to end metric

if to_metric == 'm':
   final_output = in_meters * 1
elif to_metric == 'mm':
   final_output = in_meters * 1000
elif to_metric == 'cm':
   final_output = in_meters * 100
elif to_metric =='mi':
   final_output = in_meters * 0.000621371192
elif to_metric == 'in':
   final_output = in_meters * 39.3700787
elif to_metric == 'km':
   final_output = in_meters * 0.001
elif to_metric == 'ft':
   final_output = in_meters * 3.2808399
elif to_metric == 'yd':
   final_output = in_meters * 1.0936133

print(final_output, to_metric)
