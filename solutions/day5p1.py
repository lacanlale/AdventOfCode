import logging as log
with open('../input/day5_input.txt', 'r') as file_input:
    polymer_input = list([polymer for polymer in file_input][0])


def remove_reactants(arr):
    index = 1
    while index <= len(arr)-2:
        if arr[index].lower() == arr[index-1].lower() and not(arr[index] == arr[index-1]):
            del arr[index]
            del arr[index-1]
        index += 1
    return arr

log.basicConfig(level='DEBUG')
iter_count = 1
original_length = len(polymer_input)
polymer_input = remove_reactants(polymer_input)
log.info(f"ITERATION {iter_count}\nOG LENGTH: {original_length}\nCURRENT LENGTH: {len(polymer_input)}")
while original_length != len(polymer_input):
    original_length = len(polymer_input)
    polymer_input = remove_reactants(polymer_input)
    iter_count += 1
    log.info(f"ITERATION {iter_count}\nOG LENGTH: {original_length}\nCURRENT LENGTH: {len(polymer_input)}")

log.info(f"!! FINAL ANSWER: {len(polymer_input)} !!")