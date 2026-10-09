import math
GARDEN_WIDTH = 75
GARDEN_LENGTH = 90

rows_parallel_to_length = GARDEN_WIDTH // 4
seeds_per_row_length = GARDEN_LENGTH // 1.5
total_seeds_length = rows_parallel_to_length * seeds_per_row_length

rows_parallel_to_width = GARDEN_LENGTH // 4
seeds_per_row_width = GARDEN_WIDTH  // 1.5
total_seeds_width = rows_parallel_to_width * seeds_per_row_width

print('Total seeds if rows parallel to length: ' + str(total_seeds_length))
print('Total seeds if rows parallel to width: ' + str(total_seeds_width))
print('Total seeds planted: ' + str(total_seeds_width))

SEEDS_PER_PACKET = 15
packets_finished = math.floor(total_seeds_width / SEEDS_PER_PACKET)
print('Total packets emptied: ' + str(packets_finished))
packets_needed = math.ceil(total_seeds_width / SEEDS_PER_PACKET)
print('Total packets needed: ' + str(packets_needed))
seeds_left_over = total_seeds_width % SEEDS_PER_PACKET
print('Number of seeds left over: ' + str(seeds_left_over))

print("Order: " + str(packets_needed) + " seed packets" + """
Deliver to:
Purple Farm
100 Mountain Tree Ln.
Farmville, MA 00000
""")

