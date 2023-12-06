from helpers import AoCHelper

input = AoCHelper.read_input_lines("Day6/inputs1.txt")
times = AoCHelper.extract_numbers_from_line(input[0])
distances = AoCHelper.extract_numbers_from_line(input[1])
games = list(zip(times, distances))

result = 1
for g in games:
    time, record = g
    result *= len([x for x in range(time) if x * (time - x) > record])

print(result)

full_time = int("".join([str(x) for x, y in games]))
full_record = int("".join([str(y) for x, y in games]))
result2 = len([x for x in range(full_time) if x * (full_time - x) > full_record])
print(result2)