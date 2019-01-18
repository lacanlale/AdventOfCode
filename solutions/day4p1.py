import pandas as pd
import logging as log
from datetime import date
from datetime import time


def sep_input(timestamps):
    '''
    Seperates input into dataframe
    PARAMETERS
    ----------
    timestamps : list
    RETURNS
    -------
    pandas.DataFrame
        DATE : datetime.date
        TIME : datetime.time
        STATUS : string
    IN ORDER BY DATE AND TIME
    '''
    data = {
        'DATE' : [],
        'TIME' : [],
        'STATUS' : []
    }
    for stamp in timestamps:
        unfrmt_date = stamp[1:stamp.index(' ')].strip()
        unfrmt_time = stamp[stamp.index(' ')+1:stamp.index(']')].strip()
        unfrmt_status = stamp[stamp.index(']')+2:].strip()

        year = int(unfrmt_date[:unfrmt_date.index('-')])
        month = int(unfrmt_date[unfrmt_date.index('-')+1:int(unfrmt_date.index('-'))+3])
        day = int(unfrmt_date[unfrmt_date.index('-')+4:])

        minute = int(unfrmt_time[unfrmt_time.index(':')+1:])
        hour = int(unfrmt_time[:unfrmt_time.index(':')])

        data['DATE'].append(date(year,month,day))
        data['TIME'].append(time(hour, minute))
        data['STATUS'].append(unfrmt_status)
        
    df = pd.DataFrame(data=data).sort_values(['DATE', 'TIME'])
    return df


def find_sleeptimes(df):
    '''
    Returns sleep times of each guard
    PARAMETERS
    ----------
    df : pandas.DataFrame
    RETURNS
    -------
    sleep_times = dict(guard# : total)
    sorted in ascending order of least to greatest
    '''
    current = 0
    prev = 0
    not_repeated = True
    sleep_times = {}
    for row in df.itertuples():
        time_stamp = row.TIME
        status = row.STATUS
        if 'Guard' in status:
            temp = status[status.index("#"):]
            guard_num = temp[1:temp.index(' ')]
            not_repeated = True
        elif not_repeated and 'falls' in status:
            prev = current
            current = time_stamp.minute
            not_repeated = False
        elif 'wakes' in status:
            not_repeated = True
            prev = current
            current = time_stamp.minute
            sleep_times[guard_num] = abs(current - prev) + sleep_times[guard_num] if guard_num in sleep_times else abs(current - prev)

    return sorted(sleep_times.items(), key=lambda x: x[1])


with open('../input/day4_input.txt', 'r') as file_input:
    time_input = [time for time in file_input]

log.basicConfig(level=log.DEBUG)
time_input = sep_input(time_input)
sleep_times = find_sleeptimes(time_input)
print(time_input)

sleepiest = sleep_times[-1]
guard_id = sleepiest[0]
guard_sleep_time = sleepiest[1]
sleep_min = {min: 0 for min in range(0,60)}
count_min = False
asleep = False
min_asleep = 0
min_awake = 0

for row in time_input.itertuples():
    time_stamp = row.TIME
    status = row.STATUS
    if '#' in status:
        count_min = str(guard_id) in status
    if count_min:
        if 'falls' in status:
            min_asleep = time_stamp.minute
        elif 'wakes' in status:
            min_awake = time_stamp.minute
            if(min_awake > min_asleep):
                for min in range(min_asleep, min_awake):
                    sleep_min[min] += 1
            else:
                log.debug("over")
                for min in range(min_asleep, 60):
                    sleep_min[min] += 1
                for min in range(0, min_awake):
                    sleep_min[min] += 1

sleep_min = sorted(sleep_min.items(), key=lambda x: x[1])
common_min = sleep_min[-1][0]
print(f'Guard #{guard_id} slept for a total of {guard_sleep_time} minutes, sleeping the most on minute {common_min}.')
ans = int(guard_id) * common_min
print(f'Answer: {ans}')