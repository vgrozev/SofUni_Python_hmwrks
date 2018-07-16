n = int(input())

first_line = "." * (n + 1) + "_" * (2 * n + 1) + "." * (n + 1)

print(first_line)

for i in range(n):
    print("." * (n - i) + "//" + "_" * ((2 * n - 1) + (2 * i)) + "\\\\" + "." * (n - i))

print("//" + "_" * ((4 * n - 6) // 2) + "STOP!" + "_" * ((4 * n - 6) // 2) + "\\\\")

for j in range(n):
    print("." * j + "\\\\" + "_" * ((4 * n - 1) - (2 * j)) + "//" + "." * j)
