import time


def get_corners(area):
    a, b, c, d = area.split()
    x1, x2 = map(int, str(c[2:-1]).split(".."))
    y1, y2 = map(int, str(d[2:]).split(".."))

    return x1, x2, y1, y2


def get_trajectory(x_vel, y_vel, target):
    res = False
    x1, x2, y1, y2 = get_corners(target)
    x = y = 0
    traj = [(x, y)]

    while x < x2 and (x_vel != 0 or y >= y1):
        x += x_vel
        y += y_vel
        traj.append((x, y))

        if x1 <= x <= x2 and y1 <= y <= y2:
            res = True
            break

        x_vel -= (x_vel // abs(x_vel)) if x_vel != 0 else 0
        y_vel -= 1

    return res, traj


start_time = time.time()

# input = 'target area: x=20..30, y=-10..-5'
input = "target area: x=288..330, y=-96..-50"
x1, x2, y1, y2 = get_corners(input)
y_vel = y1
traj_res = []
valid_traj = set([])

while y_vel <= -y1:
    for x_vel in range(x2 + 1):
        res, traj = get_trajectory(x_vel, y_vel, input)

        if res:
            traj_res = traj
            valid_traj.add(traj[1])

    y_vel += 1


part_one_res = max(b for a, b in traj_res)
assert part_one_res == 4560
print(f"Part 1: {part_one_res}")

part_two_res = len(valid_traj)
assert part_two_res == 3344
print(f"Part 2: {part_two_res}")

print("--- %s seconds ---" % (time.time() - start_time))
