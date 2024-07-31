from flask import request, jsonify, Blueprint
from app import db
from app.models import Message

api = Blueprint('api', __name__)

@api.route('/get/messages/<account_id>', methods=['GET'])
def get_messages(account_id):
    messages = Message.query.filter_by(account_id=account_id).all()
    return jsonify([msg.to_dict() for msg in messages]), 200

@api.route('/create', methods=['POST'])
def create_message():
    data = request.get_json()
    message = Message(**data)
    db.session.add(message)
    db.session.commit()
    return jsonify(message.to_dict()), 201

@api.route('/search', methods=['GET'])
def search_messages():
    filters = {key: value.split(',') for key, value in request.args.items()}
    query = Message.query
    if 'message_id' in filters:
        query = query.filter(Message.message_id.in_(filters['message_id']))
    if 'sender_number' in filters:
        query = query.filter(Message.sender_number.in_(filters['sender_number']))
    if 'receiver_number' in filters:
        query = query.filter(Message.receiver_number.in_(filters['receiver_number']))
    messages = query.all()
    return jsonify([msg.to_dict() for msg in messages]), 200
