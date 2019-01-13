import numpy as np
with open('../input/day3_input.txt', 'r') as file_input:
    claim_input = [claim for claim in file_input]


def label_input(claim="#0 @ 0,0: 0X0"):
    """
    Method for separating inputs into a dictionary
    PARAMETERS
    ----------
    claim : string
        Elves claim
    RETURNS
    -------
    dict
        CLAIM_ID : int,
        ROW : int,
        COL : int,
        WIDTH : int,
        LENGTH : int
    """
    coords = claim[claim.index('@')+1:claim.index(':')].strip()
    size = claim[claim.index(':')+1:].strip()
    claim_dict = {
        'claim_id' : claim[1:claim.index(' ')],
        'row' : int(coords[:coords.index(',')]),
        'col' : int(coords[coords.index(',')+1:]),
        'width' : int(size[:size.index('x')]),
        'length' : int(size[size.index('x')+1:])
    }
    return claim_dict

# Map each claim onto the fabric and record their areas
fabric = np.full((1000,1000), 0)
claim_areas = {}
for claim in claim_input:
    elf_claim = label_input(claim=claim)
    claim_areas[elf_claim['claim_id']] = elf_claim['width'] * elf_claim['length']
    print("-= MAPPING CLAIM {} =-".format(elf_claim['claim_id']))
    for row in range(elf_claim['row'], elf_claim['row'] + elf_claim['width']):
        if row >= 1000:
            break
        for col in range(elf_claim['col'], elf_claim['col'] + elf_claim['length']):
            if col >= 1000:
                break
            fabric[row][col] = -1 if fabric[row][col] else elf_claim['claim_id']

items, counts = np.unique(fabric, return_counts=True)
repetitions = dict(zip(items, counts))

# Check for equivalent areas and repetitions
for key in claim_areas:
    if claim_areas[key] == repetitions.get(int(key), 0):
        print(f"!! ANS: {key} !!")
        break