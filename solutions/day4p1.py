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
    df = pd.DataFrame(data=data)
    return df


with open('../input/day4_input.txt', 'r') as file_input:
    time_input = [time for time in file_input]

log.basicConfig(level=log.DEBUG)
guard_stamp = {}
guard_num = 0
current = 0
prev = 0
for stamp in time_input:
    break
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