import json

f = open('../../gen/data-preparation/temp/collected_tweets_kingsday.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('id\ttext\tsource\n')

cnt = 0
for line in con:
    if (len(line)<=5): continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))


    device = obj.get('source')
    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')

    outfile.write(obj.get('id_str')+'\t'+text+'\t'+device+'\n')

print('done.')
