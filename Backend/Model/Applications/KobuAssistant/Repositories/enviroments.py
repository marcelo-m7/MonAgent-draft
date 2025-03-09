from consts import Paths as p

class User:
    def __init__(self, user_id: int, request: dict):
        self.user_id: int = user_id
        self.request: dict = request
        self.user_input: str = self.request.user_input
        self.lead = None

class DatasLoaders:
    def __init__(self, conversation_subject):
        self.basic_instructions_path = p.BASIC_INSTRUCTIONS_PATH.format(conversation_subject)
        self.assistant_instructions_path = p.ASSISTANT_INSTRUCTIONS_PATH.format(conversation_subject)
        self.data_required_path = p.DATA_REQUIRED_PATH.format(conversation_subject)
        self.basic_instructions = self._basic_instructions_loader()
        self.subject_instructions = self._subject_instructions_loader()
        self.data_required = self._data_required_loader()

    def _basic_instructions_loader(self) -> str:
        """
        Loads basic instructions.

        Returns:
            str: Basic instructions for the assistant.
        """
        with open(self.basic_instructions_path, 'r', encoding='utf-8') as file:
            basic_instructions = file.read()
        print("Basic instructions: ", self.basic_instructions_path)
        return basic_instructions
    
    def _subject_instructions_loader(self) -> str:
        """
        Loads subject-specific instructions.

        Returns:
            str: Instructions specific to the current subject.
        """
        with open(self.assistant_instructions_path, 'r', encoding='utf-8') as file:
            assistant_instructions = file.read()
        print("assistant_instructions instructions: ", self.assistant_instructions_path)
        return assistant_instructions
    
    def _data_required_loader(self) -> str:
        """
        Loads data required for the current subject.

        Returns:
            str: Data required for the current subject.
        """
        with open(self.data_required_path, 'r', encoding='utf-8') as file:
            data_required = file.read()
        # print("Data required:\n", data_required)
        print("data_required: ", self.data_required_path)
        return data_required

class ConversationEnviroment(DatasLoaders):
    def __init__(self, user: User):
        self.user_input: str = user.user_input
        self.id: int = user.user_id
        self.lead: any

        self.conversation_history: list
        self.conversation_subject: str
        self.extra_context_flag: bool = True
        self.search_kwargs: int = 4

        self.current_conversation_stage: str
        self.assistant_response_message: str
        self.assistant_reponse_orientation: str
        self.current_conversation_orientation: str

        self.conversation_options_flag: bool
        self.conversation_options: list
        super().__init__(conversation_subject=self.conversation_subject)
