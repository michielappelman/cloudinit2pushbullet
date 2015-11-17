import sys
from flask import Flask, request, abort
from datetime import datetime
from pushbullet import Pushbullet

try:
    api_key = open('apikey.txt', 'r').read().strip()
except IOError:
    print "Error accessing apikey.txt."
    sys.exit(1)

phone_home_file = 'instances.log'
app = Flask(__name__)
pb = Pushbullet(api_key)

@app.route('/')
def home():
    abort(401)

@app.route('/<instance>', methods=['POST'])
def get(instance):
    with open(phone_home_file, "a") as file:
        message = "%s: VM \'%s\' (%s) is done.\n" % ( str(datetime.now()),
                   request.form['hostname'], request.form['instance_id'] )
        file.write(message)
        push = pb.push_note("VM done", message)
    return "Thanks!"

if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5100, debug=True)
    app.run(host='0.0.0.0', port=5100)
