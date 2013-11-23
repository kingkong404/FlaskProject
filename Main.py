__author__ = 'Steven'

import requests
import simplejson as json
from flask import Flask
from flask import render_template


api = requests.get('https://api.github.com/zen')

quote = api.text

request = requests.get('https://api.github.com/search/users?q=repos:%3E42+followers:%3E1000')

response = json.loads(request.text)

data = response['items']

for user in data:
    profile = requests.get('https://api.github.com/users/' + user['login'])
    dictpro = json.loads(profile.text)
    print dictpro['email']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', response=data, quote=quote),

if __name__ == '__main__':
    app.run()

app.run(debug=True)