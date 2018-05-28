n = int(input())

dragonHatchingValue = float(input())

sum_points = 0.0


for line in range(n):

    dragonsHatched, teamMembersCount = input().split()

    team_dev = int(dragonsHatched) / int(teamMembersCount)
    sum_points = sum_points + team_dev

if dragonHatchingValue == 0:
    print("{:.3f}".format(sum_points))
else:
    print("{:.3f}".format(sum_points/dragonHatchingValue))

