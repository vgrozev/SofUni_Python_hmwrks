n = int(input())

mid_p = ((2 * n) - ((n // 2) * 2 + 4))
top = "/" + "^" * (n // 2) + "\\" + "_" * mid_p + "/" + "^" * (n // 2) + "\\"
inside = "|" + " " * (2 * n -2) + "|"
bottom = "\\" + "_" * (n // 2) + "/" + " " * mid_p + "\\" + "_" * (n // 2) + "/"

print(top)

if n < 5:
    for i in range(n - 2):
        print(inside)
else:
    for i in range(n - 3):
        print(inside)
    print("|" + " " * (n//2 + 1) + "_" * mid_p + " " * (n//2 + 1) + "|")

print(bottom)
