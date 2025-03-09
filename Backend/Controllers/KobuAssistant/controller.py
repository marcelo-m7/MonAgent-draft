from Models.Applications.KobuAssistant.interface import KobuAssistant
from Models.Applications.KobuAssistant.Repositories.enviroments import ConversationEnviroment, User
import json

model = KobuAssistant()
actived_conversations = {}

def conversation_builder(user_id: int, user_request: json) -> ConversationEnviroment:
    user = User(user_id=user_id, user_request=user_request)
    cv = ConversationEnviroment(user_instance=user)
    return cv

def assistant_response_formater(cv: ConversationEnviroment) -> json:
    conversation = cv.__dict__
    attributes = {
        key: valor for key, valor in vars(conversation.__class__).items()
        if not callable(valor) and not key.startswith('__')
    }
    assistant_response = {**attributes, **conversation}
    return json.dumps(assistant_response, indent=4)

async def interface_controller(user_request: json) -> json:
    user_id: int = user_request.get('user_id')
    user_input: str = user_request.get('user_input')

    if user_id in actived_conversations:
        cv: ConversationEnviroment = actived_conversations[user_id]
        cv.user_input = user_input
    else:
        cv: ConversationEnviroment = conversation_builder(user_id=user_id, user_request=user_request)

    model_response = await model.controller(cv=cv)
    return assistant_response_formater(model_response)
