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

print('Subject,Start date,Start time', file=cal_file)

for _, row in data.iterrows():
    if not (row['title'] in list(top_conferences['title'])):
        continue

    index = top_conferences['title'] == row['title']

    other_data = top_conferences.loc[index].iloc[0]

    print('HELLO')
    print(row['deadline'])
    print(other_data['title'])
    print(','.join(
        [other_data['title'] + ' submission deadline'] +
        str(row['deadline']).split(' ')),
        file=cal_file)

