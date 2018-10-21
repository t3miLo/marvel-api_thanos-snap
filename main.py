from flask import Flask, render_template, url_for
import requests
import time
import hashlib
import json
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'djdkajgd839'


def getCharacterData():

    # check if data has already locally
    charExist = os.path.isfile('charData.json')
    if charExist:
        with open('charData.json') as f:
            characterData = json.load(f)
            return characterData
    else:
        ts = str(int(time.time()))
        public_key = '54d7b69dcd93a381909d5c7f8494d03c'
        private_key = 'Private Key would go here'
        keyHash = (ts + private_key + public_key).encode('utf-8')
        hassh = hashlib.md5(keyHash).hexdigest()

        payload = {'ts': ts, 'apikey': public_key, 'hash': hassh}
        allChars = requests.get(
            'https://gateway.marvel.com/v1/public/events/29/characters?limit=60', params=payload)

        print(allChars.raise_for_status())
        print(allChars.status_code)
        characterData = allChars.json()

        with open('charData.json', 'w') as outfile:
            json.dump(characterData, outfile)

        return characterData


@app.route('/')
def index():
    charsInfo = {}
    charPotrait = getCharacterData()
    for potrait in charPotrait['data']['results']:
        if potrait['id'] not in [1009652, 1009165, 1009726, 1009299]:
            name = potrait['name']

            newName = re.sub(r'\(.*\)', '', name)
            charsInfo[newName] = (potrait['thumbnail']
                                  ['path'] + '/standard_medium.jpg')

    return render_template('index.html', charsInfo=charsInfo)


if __name__ == '__main__':
    app.run()


# infinity war even
# https://gateway.marvel.com:443/v1/public/events/29/characters?limit=60&apikey=54d7b69dcd93a381909d5c7f8494d03c
# Thanos
# http://i.annihil.us/u/prod/marvel/i/mg/6/40/5274137e3e2cd/standard_medium.jpg
