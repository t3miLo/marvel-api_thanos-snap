from flask import Flask, render_template
import requests
import time
import hashlib


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Jeremiah1010'

ts = str(int(time.time()))
public_key = '54d7b69dcd93a381909d5c7f8494d03c'
private_key = 'cfd54158ee1fe84ddefc5e4982ee7815853d4511'
keyHash = (ts + private_key + public_key).encode('utf-8')
hassh = hashlib.md5(keyHash).hexdigest()

payload = {'ts': ts, 'apikey': public_key, 'hash': hassh}
allChars = requests.get(
    'https://gateway.marvel.com/v1/public/events/29/characters?limit=60', params=payload)

print(allChars.raise_for_status())
print(allChars.status_code)
charData = allChars.json()

print(charData)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


# infinity war even
# https://gateway.marvel.com:443/v1/public/events/29/characters?limit=60&apikey=54d7b69dcd93a381909d5c7f8494d03c
# Thanos
# https://gateway.marvel.com:443/v1/public/characters?name=Thanos&apikey=54d7b69dcd93a381909d5c7f8494d03c
