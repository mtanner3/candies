
import sys

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

LOL = []
LOL.append( (0, rank_arr) )

while True:
    print "=" * 20
    for thislist in LOL:
        print "-" * 5
        offset = thislist[0]
        thislist = thislist[1]
        print "at offset %d; thislist: %s" % (offset, thislist)
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

