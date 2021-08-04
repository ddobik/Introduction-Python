import json

with open('acdc.json', 'r') as file:
    file_dict = json.load(file)
    file_dict1 = file_dict['album']['tracks']['track']
    sum_duration = 0
    for track in file_dict1:
        sum_duration += int(track['duration'])
    print('Общая длительность треков', ':', sum_duration, 'секунд')

import datetime

print(str(datetime.timedelta(seconds=sum_duration)))

