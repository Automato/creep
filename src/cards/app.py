from flask import Flask
from flask.ext.stormpath import StormpathManager, login_required
from redis import StrictRedis
import uuid

app = Flask(__name__)
app.debug = True #FIXME
app.config['SECRET_KEY'] = '' #TODO: add key
app.config['STORMPATH_API_KEY_ID'] = ''
app.config['STORMPATH_API_KEY_SECRET'] = ''
app.config['STORMPATH_ENABLE_GOOGLE'] = True
app.config['STORMPATH_SOCIAL'] = {
    'GOOGLE': {
        'client_id': '',
        'client_secret': '',
    }
}
app.config['STORMPATH_APPLICATION'] = 'Creep'
redis = StrictRedis(host=app.config.get('REDIS_HOST'), port=app.config.get('REDIS_PORT'), db=0)
stormpath_manager = StormpathManager(app)

@app.route('/', methods=['GET'])
@login_required
def list_cards():
    return str(redis.hgetall('cards'))

@app.route('/', methods=['POST'])
@login_required
def create_card():
    card_id = uuid.uuid4()
    redis.hset('cards', str(card_id), str(request.body))
    return "add card here. Card allegedly posted as " + str(card_id)

@app.route('/<uuid:card_id>', methods=['GET'])
@login_required
def retrieve_card(card_id):
    return str(redis.hget('cards', 'card_id))

@app.route('/<uuid:card_id>', methods=['PATCH', 'PUT'])
@login_required
def replace_card(card_id):
    redis.hset('cards', str(card_id), str(request.body))
    return "replace card here. Card allegedly replaced"

@app.route('/<uuid:card_id>', methods=['DELETE'])
@login_required
def delete_card(card_id):
    redis.hdel('cards', str(card_id))
    return "delete card here. Card allegedly deleted"

app.run(host='0.0.0.0')
