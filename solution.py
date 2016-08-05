
num_children = int(raw_input().strip())
rank_arr = []
candy_arr = []
rank_location = {}
for idx in range(num_children):
    rank = int(raw_input().strip())
    rank_arr.append(rank)
    if rank not in rank_location.keys():
        rank_location[rank] = []
    rank_location[rank].append(idx)
    candy_arr.append

print rank_arr
rank_values = rank_location.keys()
rank_values.sort()
rank_values.reverse()
lows = rank_location[rank_values.pop()] # remove the lowest scores. They already have 1 candy
print lows
new_lists = []
left_low = 0
for low in lows:
    pass


