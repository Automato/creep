from flask import Flask

from flask.ext.stormpath import StormpathManager

app = Flask(__name__)
app.debug = True #FIXME
app.config['SECRET_KEY'] = '' #TODO: add key
app.config['STORMPATH_API_KEY_ID'] = ''
app.config['STORMPATH_API_KEY_SECRET'] = ''
app.config['STORMPATH_APPLICATION'] = ''

stormpath_manager = StormpathManager(app)

@app.route('/')
def home():
    return ""

app.run(host='0.0.0.0')
