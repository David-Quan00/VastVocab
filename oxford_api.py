#oxford_api = '65e664d4'

#python -m pip install requests

import requests
import json
import pprint
import flask

app_id = '65e664d4'
app_key = '7ede5606bf2c1551bafc98676fd4bac9'

language = 'en'
word_id = 'selfie'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()

r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))

data = json.dumps(r.json())

jsonToPython = json.loads(data)

#The pp will make indent the json file so it is easily readable
pp = pprint.PrettyPrinter(indent=4)
pp.pprint (jsonToPython)

for word in jsonToPython['results']:
    theWord = word['id']
    print("Word:", theWord)
    #print(word['definitions'])

for word in jsonToPython['results']:
    for entries in (word['lexicalEntries']):
        for deff in (entries['entries']):
            for line in (deff['senses']):
                if line == "," or line == "[" or line == "]":
                    print("")
                else:
                    theDefinition = line["definitions"]
                    print("Definition:", theDefinition)

#Info to export to html
