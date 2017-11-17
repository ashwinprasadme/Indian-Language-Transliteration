from flask import Flask,render_template, send_from_directory, request, redirect
from indictrans import Transliterator
import imgkit
import time
from datetime import datetime
from pymobird import SimplePymobird, Content

# init client
bird = SimplePymobird(ak='00', device_id='00')

options = {
    'format': 'jpg',
    'crop-x': '0',
    'crop-y': '0',
    'crop-w': '620'
}

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/get/<name>')
def generate(name):
    print "start"
    result = imgkit.from_url('http://127.0.0.1:5001/{}'.format(name), './static/{}.jpg'.format(name), options=options)
    print result
    return send_from_directory('static', '{}.jpg'.format(name))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        generate(request.form['name'])
        return redirect("/preview/{}".format(request.form['name'])) 
    else:
        return render_template('index.html')    


@app.route('/preview/<name>', methods=['GET'])
def preview(name):
    return render_template('preview.html', name=name)    
    

@app.route('/print', methods=['POST'])
def printImage():
    content = Content()
    content.add_image("./static/{}.jpg".format(request.form['name']))
    content.add_text(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    content_id = bird.print_multi_part_content(content)
    wait = 0
    while (not bird.check_printed(content_id)) and (wait < 5) :
        time.sleep(3)
        wait += 1
        print wait
    return redirect("/") 
    
