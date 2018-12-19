with open('../input/day1_input.txt', 'r') as freq:
    freq_input = [x.strip() for x in freq]

freqs_overtime = []
calc_freq = 0
loop = 1
repeated = False
while not repeated:
    print("Loop: ", loop)
    for freq in freq_input:
        if freq[0] == '-':
            calc_freq -= int(freq[1:])
        else:
            calc_freq += int(freq[1:])

        if calc_freq in freqs_overtime:
            print("First duplicate frequency: ", calc_freq)
            repeated = False
            break
        freqs_overtime.append(calc_freq)
    loop += 1
