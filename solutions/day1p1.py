with open('../input/day1_input.txt', 'r') as freq:
    freq_input = [x.strip() for x in freq]

final_freq = 0
for freq in freq_input:
    if freq[0] == '-':
        final_freq -= int(freq[1:])
    else:
        final_freq += int(freq[1:])

print(final_freq)