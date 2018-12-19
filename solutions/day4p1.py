with open('../input/day4_input.txt', 'r') as file_input:
    time_input = [time for time in file_input]

guard_stamp = {}
guard_num = 0
current = 0
prev = 0
for stamp in time_input:
    if '00:' in stamp:
        if 'Guard' in stamp:
            temp = stamp.index("#")
            guard_num = stamp[temp[1:temp.index(' ')].trim()]
        elif 'falls' in stamp:
            prev = current
            current = int(stamp[stamp.index(':'):stamp.index(']')])
        else:
            prev = current
            current = int(stamp[stamp.index(':'):stamp.index(']')])-1
            guard_stamp[guard_num] += current - prev