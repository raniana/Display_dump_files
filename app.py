from flask import Flask, render_template
import data
app = Flask(__name__)

event1 = data.Data("1","07.17.2017","12:45","initializing the tool")
event2 = data.Data("2","07.17.2017","01:45","first reading")

events = [event1,event2]        

@app.route('/display')
def displayDumpFile():
	return render_template('showEvents.html',events=events)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	
