from abc import ABC


class User:
    def __init__(self, user_id=int, request=dict, conversation_assistant=str):
        self.user_id = user_id
        self.conversation_assistant = conversation_assistant
        self.request = request


class Enviroment(ABC, User):
    def __init__(self, user_id=int, new_request=dict):
        super().__init__(user_id=user_id, request=new_request)
        self.conversation_history = list
        self.conversation_subject = str
        self.conversation_orientation = str

        self.options = bool
        self.current_stage = str
        self.previous_stage = str
        self.next_stage = str

        self.previous_response = dict
        self.current_response = dict

        self.previous_request = dict
        self.current_request = dict
        self.user_input = str(self.current_request.user_input)


class ConversationEnviroment(Enviroment):
    def __init__(self):
        super().__init__()

    @property
    def request(self):
        return self.request
    
    @request.setter
    def request(self, request):
        if request:
            self.previous_request = self.current_request
            self.current_request = request
            self._refresh_enviroment(request=request)
        return self.current_request
    
    def _refresh_enviroment(self, request):
        """
        Updates the class attributes based on the keys and values provided in the dictionary.

        :param request: Dictionary containing the updates for the class attributes.
        """
        if not isinstance(request, dict):
            raise ValueError("The 'request' parameter must be a dictionary.")

        for key, value in request.items():
            if hasattr(self, key):  # Checks if the attribute exists in the class
                setattr(self, key, value)  # Updates the attribute value
            else:
                print(f"Attribute '{key}' does not exist in the class and will be ignored.")
                