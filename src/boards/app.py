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
def list_boards():
    return ""

@app.route('/', methods=['POST'])
@login_required
def create_board():
    return "add board here"

@app.route('/<uuid:board_id>', methods=['GET'])
@login_required:
def retrieve_board(card_id):
    return "get board here"

@app.route('/<uuid:board_id>', methods=['PATCH', 'PUT'])
@login_required:
def replace_board(board_id):
    return "replace board here"

@app.route('/<uuid:board_id>', methods=['DELETE'])
@login_required:
def delete_board(board_id):
    return "delete board here"

app.run(host='0.0.0.0')
