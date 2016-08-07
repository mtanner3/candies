
import sys

rank_arr = []
candy_arr = []
MAX_RANKING = 10**5

num_children = int(raw_input().strip())
# read in the student rankings, initialize rank_arr and candy_arr
# also find the minimum ranking
minrank = MAX_RANKING + 1
for idx in range(num_children):
    rank = int(raw_input().strip())
    rank_arr.append(rank)
    if rank < minrank:
        minrank = rank
    candy_arr.append(0)

def done():
    for idx in range(num_children):
        if candy_arr[idx] == 0:
            return False
    return True
    
def get_candy_count():
    return sum(candy_arr)

def print_candies():
    print "%7s %7s" % ("Rank", "Candies")
    print "%7s %7s" % ("-" * 7, "-" * 7)
    for idx in range(num_children):
        print "%7s %7s" % (rank_arr[idx], candy_arr[idx])

#minrank = min(rank_arr) # faster than tracking this while reading input?
# give one candy to all the min-rank students
for idx in range(num_children):
    if rank_arr[idx] == minrank:
        candy_arr[idx] = 1

# split the list into sublists on min-rank student boundaries
LOL = []

offset = 0
tmplist = []
for idx in range(num_children):
    if candy_arr[idx] == 1:
        if len(tmplist) > 0:
            LOL.append( (offset, tmplist) )
        tmplist = []
        offset = idx+1
    else:
        tmplist.append(rank_arr[idx])
if len(tmplist) > 0:
    LOL.append( (offset, tmplist) )

print LOL

new_LOL = []
while len(LOL) > 0:
    entry = LOL.pop()
    offset = entry[0]
    sublist = entry[1]
    if len(sublist) == 2:
        if offset == 0 and (sublist[0] <= sublist[1]):
            candy_arr[offset] = 1
        if offset == (num_children-1) and (sublist[1] <= sublist[0]):
            candy_arr[offset+1] = 1

    elif len(sublist) == 1:
        if offset == 0: 
            if sublist[0] > rank_arr[offset+1]:
                candy_arr[offset] = candy_arr[offset+1] + 1
        if offset == (num_children-1):
            candy_arr[offset+1] = 1




        if sublist[offset] > rank_arr[offset-1]:
            candy_arr[offset] = candy_arr[offset-1] + 1
        else:
            candy_arr[offset] = 1



"""


# set up left edge
if minrank_arr[minrank] == 0:
    minrank_arr.pop(0)
if minrank_arr[minrank] == 1:
    minrank_arr.pop(0)
# set up the right edge
minrank_arr.append(len(rank_arr)-1)

left_edge = 0
for right_edge in minrank_arr:
    left_edge += 1
    if right_edge > (left_edge + 1):
        tmplist = []
        for rankval in rank_arr[left_edge:right_edge]:
            tmplist.append(rankval)
        LOL.append((left_edge, tmplist))
    left_edge = right_edge
LOL.append((left_edge, tmplist))
print LOL

sys.exit(0)

while left_edge in rank_location[minrank]:
    left_edge += 1


    if idx > 0 and idx < num_children - 1:
        if candy_arr[idx] == 1:
            continue
        if left_edge is None:
            left_edge = idx
            tmplist.append(this_rank)

print_candies()



LOL.append( (0, rank_arr) )

while True:
    print "=" * 20
    for thislist in LOL:
        print "-" * 5
        offset = thislist[0]
        thislist = thislist[1]
        print "at offset %d; thislist: %s" % (offset, thislist)
        # find the low value for this list
        # give them each 
        lowval = min(thislist)
        print "low val is: %d" % lowval
        newlists = []
        tmplist = []
        newoffset = None
        for idx, element in enumerate(thislist):
            if element > lowval:
                tmplist.append(element)
                if newoffset is None:
                    newoffset = idx + offset
            else:
                if len(tmplist) > 3:
                    newlists.append( (newoffset, tmplist) )
                else:
                    print "handle as a base case: %s" % tmplist
                tmplist = []
                newoffset = None
        if len(tmplist) > 3:
            newlists.append( (newoffset, tmplist) )
        else:
            print "handle as a base case: %s" % tmplist
            
        print newlists
        LOL = newlists
    if len(LOL) == 0: 
        break

sys.exit(0)


rank_values = rank_location.keys()
rank_values.sort()
rank_values.reverse()

lows = rank_location[rank_values.pop()] # remove the lowest scores. They already have 1 candy
print lows
if lows[0] == 0: # get rid of a 'low' on the left boundary.
    lows.pop(0)
new_lists = []
left = 0
for low in lows:
    right = low
    if right == left+1:
        left = right
        continue
    new_lists.append(rank_arr[left+1:right])
    left = right
right = len(rank_arr)
# need a check here for left and right being the same thing
new_lists.append(rank_arr[left+1:right])

print "new lists:"
print new_lists
"""
