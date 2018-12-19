from collections import Counter

with open('../input/day2_input.txt', 'r') as id_list:
    id_input = [box_id for box_id in id_list]

doub = 0
trip = 0
for box_id in id_input:
    rep_dict = dict(Counter(box_id))
    values = list(rep_dict.values())
    if 2 in values:
        doub += 1
    if 3 in values:
        trip += 1

print("Checksum: ", (doub*trip))