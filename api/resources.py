from flask import request
from flask_restx import Resource
from . import api
from models import Conversation, create_conversation, get_conversations, create_segment

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'from blueprint!'}


@api.route('/get_conversations', methods=['GET'])
class GetConversations(Resource):
    def get(self):
        conversations = get_conversations()
        return [{'id': conversation.id, 'name': conversation.name} for conversation in conversations]

@api.route('/get_conversation/<int:id>', methods=['GET'])
class GetConversation(Resource):
    def get(self, id):
        conversation = Conversation.query.get(id)
        return {'id': conversation.id, 'name': conversation.name, 'created_date': conversation.created_date.isoformat()}

@api.route('/new_conversation', methods=['POST'])
class NewConversation(Resource):
    def post(self):
        try:
            data = request.get_json()
            conversation = create_conversation(data.get('name', ''))
            return {'conversation_id': conversation.id}
        except Exception as e:
            return {'error': str(e)}
    
        
@api.route('/message', methods=['POST'])
class Message(Resource):
    def post(self):
        data = request.get_json()
        conversation_id = data.get('conversation_id')
        message = data.get('message')
        #create the next segment in the conversation
        segment = create_segment(conversation_id, message)

        return {'received message': data.get('message', 'no message was provided') + 'from segment ' + str(segment.id) + ' in conversation ' + str(conversation_id)}
    
@api.route('/get_segments/<int:id>', methods=['GET'])
class GetSegments(Resource):
    def get(self, id):
        conversation = Conversation.query.get(id)
        segments = conversation.segments
        return [{'id': segment.id, 'message': segment.message, 'reply': segment.reply} for segment in segments]