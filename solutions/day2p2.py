with open('../input/day2_input.txt', 'r') as id_list:
    id_input = [box_id for box_id in id_list]

for box_id in id_input:
    diffs = 0
    found = True
    for letter in box_id:
        for next_id in id_input:
            if box_id == next_id:
                next(id_input)
            else:
                for n_letter in next_id:
                    if n_letter != letter:
                        diffs += 1
                    if diffs >= 2:
                        found = False
                        break

