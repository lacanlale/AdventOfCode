import numpy as np
import logging as log


def remove_reactants(arr):
    index = 1
    while index <= len(arr)-2:
        if arr[index].lower() == arr[index-1].lower() and not(arr[index] == arr[index-1]):
            del arr[index]
            del arr[index-1]
        index += 1
    return arr


def remove_instances(letter, arr):
    arr = list(filter(lambda a: a != letter.upper(), arr))
    return list(filter(lambda a: a != letter.lower(), arr))


with open('../input/day5_input.txt', 'r') as file_input:
    polymer_input = list([polymer for polymer in file_input][0])

log.basicConfig(level='DEBUG')
alphas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphas = {key : 0 for key in alphas}
for letter in alphas:
    log.debug(f'CURRENT LETTER: {letter}')
    altered_poly = remove_instances(letter, polymer_input)
    original_length = len(altered_poly)
    altered_poly = remove_reactants(altered_poly)
    while original_length != len(altered_poly):
        original_length = len(altered_poly)
        altered_poly = remove_reactants(altered_poly)
    alphas[letter] = len(altered_poly)

log.info(f"!! ANS: LETTER {min(alphas, key=alphas.get)} WITH LENGTH {alphas[min(alphas, key=alphas.get)]}")