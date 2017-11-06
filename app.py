from flask import Flask, render_template, request, url_for
from werkzeug import secure_filename
import data
app = Flask(__name__)

event1 = data.Data("1","07.17.2017","12:45","initializing the tool")
event2 = data.Data("2","07.17.2017","01:45","first reading")

events = [event1,event2]        

@app.route('/display')
def displayDumpFile():
	return render_template('showEvents.html',events=events)


@app.route('/upload')
def choose_file():
	return render_template('loadFile.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
   else:
           return "please choose a file"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	
