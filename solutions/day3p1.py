import numpy as np
with open('../input/day3_input.txt', 'r') as file_input:
    claim_input = [claim for claim in file_input]


def label_input(claim=""):
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

fabric = np.full((1000,1000), 0)
for claim in claim_input:
    elf_claim = label_input(claim=claim)
    print("-= MAPPING CLAIM {} =-".format(elf_claim['claim_id']))

    for row in range(elf_claim['row'], elf_claim['row'] + elf_claim['length']):
        if row >= 1000:
            break
        for col in range(elf_claim['col'], elf_claim['col'] + elf_claim['width']):
            if col >= 1000:
                break
            fabric[row][col] = 9 if fabric[row][col] else 1

print(np.unique(fabric, return_counts='True'))