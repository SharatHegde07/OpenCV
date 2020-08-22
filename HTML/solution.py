import urllib.request
import json

url = input('Enter location:')
print('Retrieving',url)

data = urllib.request.urlopen(url).read().decode()

print('Retrieved',len(data),'characters')

js = json.loads(data)

sum=0
count=0

for i in js['comments']:
    x = int(i['count'])
    sum+=x
    count+=1
print('Count:',count)
print('Sum:',sum)
