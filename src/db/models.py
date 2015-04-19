from app import db
from sqlalchemy.dialects.postgresql import JSON, UUID

class Board(db.Model):
    board_id = db.Column(UUID)
    name = db.Column(db.String(128))

class Card(db.Model):
    card_id = db.Column(UUID)
    body = db.Column(JSON)
    board_id = db.Column(UUID, db.ForeignKey('Board.board_id'))
