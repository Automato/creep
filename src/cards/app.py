from flask import Flask
from flask.ext.stormpath import StormpathManager

app = Flask(__name__)
app.debug = True #FIXME
app.config['SECRET_KEY'] = '' #TODO: add key
app.config['STORMPATH_API_KEY_ID'] = ''
app.config['STORMPATH_API_KEY_SECRET'] = ''
app.config['STORMPATH_APPLICATION'] = ''

stormpath_manager = StormpathManager(app)

@app.route('/', methods=['GET'])
@login_required
def list_cards():
    return "cards go here"

@app.route('/', methods=['POST'])
@login_required
def create_card():
    return "add card here"

@app.route('/<uuid:card_id>', methods=['GET'])
@login_required:
def retrieve_card(card_id):
    return "get card here"

@app.route('/<uuid:card_id>', methods=['PATCH', 'PUT'])
@login_required:
def replace_card(card_id):
    return "replace card here"

@app.route('/<uuid:card_id>'. methods=['DELETE'])
@login_required:
def delete_card(card_id):
    return "delete card here"

app.run(host='0.0.0.0')
