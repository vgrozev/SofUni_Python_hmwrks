bla_list = [23.3, 13.0, 55.7, 67.0]

#print(', '.join(bla_list))

#print(*bla_list)
# for item in bla_list:
#     print("{0:g}".format(item), end='')









#print(" ".join('%g' % item for item in bla_list))



# print(" ".join(


bla = ["{:g}".format(item) for item in bla_list]
bla_2 = " ".join(bla)
print(bla_2)
