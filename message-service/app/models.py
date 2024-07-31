from app import db
from sqlalchemy.dialects.mysql import VARCHAR
import uuid

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(VARCHAR(36), nullable=False)
    message_id = db.Column(VARCHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    sender_number = db.Column(VARCHAR(15), nullable=False)
    receiver_number = db.Column(VARCHAR(15), nullable=False)

    def to_dict(self):
        return {
            'account_id': self.account_id,
            'message_id': self.message_id,
            'sender_number': self.sender_number,
            'receiver_number': self.receiver_number
        }
