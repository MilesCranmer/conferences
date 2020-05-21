import yaml
import pandas as pd

data = None
with open("conferences.yml", 'r') as stream:
    try:
        data = pd.DataFrame(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

top_conferences = pd.read_csv('top_conferences.csv')

cal_file = open('calendar.csv', 'w')

print('Subject,Start Date,All Day Event,Description,', file=cal_file)

for _, row in data.iterrows():
    if not (row['title'] in list(top_conferences['title'])):
        continue

    index = top_conferences['title'] == row['title']

    other_data = top_conferences.loc[index].iloc[0]

    modifier = ''
    for year_update in range(3):
        date = row['deadline'].split(' ')[0]
        if year_update > 0:
            modifier = ' [expected]'
            tmp = date.split('-')
            date = '-'.join([
                str(int(tmp[0]) + year_update),
                tmp[1],
                tmp[2]])

        print(','.join(
            [other_data['title'] + modifier + ' submission deadline'] +
            [
                date,
                'True',
                (other_data['description'] +
                    ' - h-index=' +
                    str(other_data['h-index']) +
                    ' ' +
                    row['link'])
            ]),
            file=cal_file)

