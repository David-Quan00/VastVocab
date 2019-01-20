#Flaskblog.py file

from flask import Flask, request, render_template
import requests
import json
import pprint
from random import randint

app = Flask(__name__)

#Two possible routes, nothing after the slash and 'home'
words = [
    'laceration',
    'gauze',
    'microbiology',
    'Anthropology',
    'Pharmacology',
    'scalpel',
    'endocrine',
    'abdominal',
    'abdominoplasty',
    'tendon',
    'adhesion',
    'aneurysm',
    'angioplasty',
    'neurofibroma',
    'asymptomatic',
    'biopsy',
    'benign',
    'bradycardia',
    'bronchitis',
    'carcinogenic',
    'cerebrum',
    'chemotherapy',
    'chronic',
    'uranoplasty',
    'dermatitis',
    'diagnosis',
    'diaphragm',
    'disease',
    'Thoracic',
    'Umbilical']
@app.route("/", methods=['GET','POST'])
@app.route("/home")
def home():

    rand = randint(0, 29)
    word = words[rand]

    counter = True

    while counter == True:

        app_id = '65e664d4'
        app_key = '7ede5606bf2c1551bafc98676fd4bac9'

        language = 'en'
        word_id = word

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        #print("code {}\n".format(r.status_code))
        #print("text \n" + r.text)
        # print("json \n" + json.dumps(r.json()))

        data = json.dumps(r.json())

        jsonToPython = json.loads(data)

        # The pp will make indent the json file so it is easily readable
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(jsonToPython)

        string1 = ""
        string2 = ""

        for word in jsonToPython['results']:
            theWord = word['id']
            #print("Word:", theWord)
            string1 = theWord
            # print(word['definitions'])


        for word in jsonToPython['results']:
            for entries in (word['lexicalEntries']):
                for deff in (entries['entries']):
                    for line in (deff['senses']):
                        if 2 > 1:
                            theDefinition = line["definitions"]
                            #print("Definition:", theDefinition)
                            string2 = theDefinition

        theAnswer = str(string1 + ": " + str(string2))
        counter == False
        return render_template('home.html', theAnswer=theAnswer)

    #return (theAnswer)
    # request for json
    # then parse
    # word = parsed_word
    #return render_template('home.html', word=word)
    
    

#Change the subdomain and the function
@app.route("/generate")
def generate():

    return ("")
    

if __name__ == "__main__":
    app.run(debug=True)
