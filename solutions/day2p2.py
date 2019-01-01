import logging as log
from difflib import ndiff

with open('../input/day2_input.txt', 'r') as id_list:
    id_input = [box_id for box_id in id_list]

log.basicConfig(level=log.DEBUG)
id_input.sort()
index = 0
while id_input:
    box_id = id_input[0]
    for next_id in id_input:
        if box_id != next_id:
            diffs = [x for x in range(len(box_id)-1) if box_id[x] != next_id[x]]
            # log.debug(diffs)
            if len(diffs) == 1:
                word1 = set(box_id)
                word2 = set(next_id)
                diff = word1-word2
                print(f'Remove {diff} from {box_id}')
                break
    id_input.remove(box_id)