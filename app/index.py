#app.py

from flask import Flask, request #import main Flask class and request object
import requests
from flask_bootstrap import Bootstrap
import random
import getpass
import arrow
import os
import subprocess
import random
myusr = getpass.getuser()
app = Flask(__name__) #create the Flask app
Bootstrap(app)

from flask import render_template



@app.route('/', methods=['GET', 'POST'])
def form(name=None):
    if request.method == 'POST':  #this block is only entered when the form is submitted
        blogpath = request.form.get('blogpath')
        blogname = request.form.get('blogname')
        postname = request.form.get('postname')
        posttag = request.form.get('posttag')
        imgpath = request.form.get('imgpath')

        timnow = arrow.now()

        #listpath = os.listdir('{}/{}'.format(blogpath, timnow.strftime('%Y'))
        if timnow.strftime('%Y') in os.listdir('{}/{}/galleries/'.format(blogpath, blogname)):
            pass
        else:
            os.mkdir('{}/{}/galleries/{}'.format(blogpath, blogname, timnow.strftime('%Y')))

        if timnow.strftime('%m') in os.listdir('{}/{}/galleries/{}'.format(blogpath, blogname, timnow.strftime('%Y'))):
            pass
        else:
            os.mkdir('{}/{}/galleries/{}/{}'.format(blogpath, blogname, timnow.strftime('%Y'), timnow.strftime('%m')))

        if timnow.strftime('%d') in os.listdir('{}/{}/galleries/{}/{}'.format(blogpath, blogname, timnow.strftime('%Y'), timnow.strftime('%m'))):
            pass
        else:
            os.mkdir('{}/{}/galleries/{}/{}/{}'.format(blogpath, blogname, timnow.strftime('%Y'), timnow.strftime('%m'), timnow.strftime('%d')))

        gallerpath = '/galleries/{}/{}/{}'.format(timnow.strftime('%Y'), timnow.strftime('%m'), timnow.strftime('%d'))

        fridpath = blogpath + '/' + blogname + gallerpath

        subprocess.call('scp -r {}/*.png {}'.format(imgpath, fridpath), shell=True)

        todayart = os.listdir(fridpath)

        todayart.sort()

        ranimg = random.choice(todayart)

        pathurl = 'http://artctrl.me/galleries/{}/{}/{}'.format(timnow.strftime('%Y'), timnow.strftime('%m'), timnow.strftime('%d'))

        if postname not in '{}/{}/posts'.format(blogpath, blogname):
            with open('{}/{}/posts/{}.meta'.format(blogpath, blogname, postname), 'w') as daympo:
                daympo.write('.. title: {}\n.. slug: {}\n.. date: {}\n.. tags: {}\n.. link:\n.. description:\n.. type: text'.format(postname, postname, timnow.datetime, posttag))

            with open('{}/{}/posts/{}.md'.format(blogpath, blogname, postname), 'w') as daymark :
                for toar in todayart:
                    daymark.write('![{}]({}/{})\n\n'.format(toar.replace('.png', ''), gallerpath, toar))





        return '''
                <img src="/static/{}{}/{}"><br>
                <h1>legal materials results</h1><br>


                  '''.format(blogname, gallerpath, ranimg)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #run app in debug mode on port 5000
