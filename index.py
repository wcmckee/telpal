#app.py

from flask import Flask, request #import main Flask class and request object
import requests
import shutil
import os
import getpass
from urllib.parse import urlparse
import PIL
import json
from PIL import ImageDraw, ImageFont
from PIL import Image
from PIL import ImageDraw
from flask_bootstrap import Bootstrap
import giphypop
import random
myusr = getpass.getuser()
app = Flask(__name__) #create the Flask app
Bootstrap(app)
g = giphypop.Giphy()



from flask import render_template

@app.route('/lodgecomplaint/')
@app.route('/lodgecomplaint/<name>')
def hello(name=None):
    reqimgz = requests.get('https://api.giphy.com/v1/gifs/search?api_key=ee58ff1d10c54fd29ddb0388126c2bcd&q=thumbsdown&limit=25&offset=0&rating=G&lang=en')
    myimg = (reqimgz.json())
    ransom = len(myimg['data'])
    ranz = random.randint(0, ransom)

    return render_template('lodgecomplaint.html', name=name, gifimg = myimg['data'][ranz]['images']['fixed_width']['url'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #run app in debug mode on port 5000
