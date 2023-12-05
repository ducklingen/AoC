from adventofcode.helpers import AoCHelper
import logging
from math import ceil
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

input = AoCHelper.read_input_lines("AoC23/Inputs/Day5/inputs.txt")
initial_seeds = AoCHelper.extract_numbers_from_line(input[0])
logging.info(initial_seeds)

groups = AoCHelper.group_lines(input[2:])

def transform_positions_min(initial_positions, groups):
    min = sys.maxsize * 2 + 1
    for s in initial_positions:
        for g in groups:
            new_pos = s
            for t in g[1:]:
                dest, src, rng = AoCHelper.extract_numbers_from_line(t)

                if src <= s <= src + rng - 1:
                    new_pos = s + (dest - src)
            
            s = new_pos
        
        if s < min:
            min = s
    
    return min

result = transform_positions_min(initial_seeds, groups)
assert result == 650599855
logging.info(f"Part 1: {result}")

initial_seeds_2 = []
for i in range(ceil(len(initial_seeds)/2)):
    start = initial_seeds[2 * i]
    initial_seeds_2.append(start)
    len = initial_seeds[2 * i+1]
    result2 = sys.maxsize * 2 + 1
    logging.info(f"Checking entries in [{start}, {start + len}]")
    min = transform_positions_min(list(range(start, start + len)), groups)
    if min < result2:
        result2 = min

logging.info(f"Part 2: {result}")