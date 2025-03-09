class Stages:
    # STAGES POSSIBLES
    WELCOME_STAGE = 'welcome'  # Welcome stage
    ACCEPTANCE_OF_TERMS_STAGE = 'acceptance_of_terms'
    CHOOSE_SUBJECT_STAGE = 'choose_subject'  # Stage to choose a subject
    DATA_COLLECTING_STAGE = 'data_colecting'  # Data collecting stage
    DATA_COLLECTING_VALIDATION_STAGE = 'data_colecting_validation'  # Data collecting validation stage
    RESUME_VALIDATION_STAGE = 'resume_validation'  # Resume validation stage
    SEND_VALIDATION_STAGE = 'send_validation'  # Send validation stage
    FREE_CONVERSATION_STAGE = 'free_conversation'  # Free conversation stage
    # OPTIONS POSSIBLES BY STAGES
    ACCEPTANCE_OF_TERMS_STAGE_OPTIONS = [
        "I agree to the terms and conditions.",
        "I do not agree to the terms and conditions."
    ]  # Options for the acceptance of terms stage
    CHOOSE_SUBJECT_STAGE_OPTIONS = [
        "I'd like to know more about KOBU Agency.",
        "I'd like to hire KOBU.",
        "I'd like to join KOBU team.",
        # "I'd like to talk to somebody in KOBU Agency."
    ]  # Options for the choose subject stage
    RESUME_VALIDATION_STAGE_OPTIONS = [
        "It looks fine!",
        "Actually I'd like to change something, if you don't mind."
    ]  # Options for the resume validation stage
    SEND_VALIDATION_STAGE_OPTIONS = [
        "Yes, you may send!",
        "Wait. Do not send it yet, please."
    ]  # Options for the send validation stage

class FlowOrientations:
    # CONVERSATION POSSIVLES ORIENTATIONS
    RESPONSE_READY = 'response_ready'
    STAGE_FINISHED = 'stage_finished'
    NEXT_STAGE = 'next_stage'  # Proceed to the next stage
    # ASSISTANT NEXT ORIENTATIONS POSSIBLES
    PROCEED = 'proceed'  # Proceed with the current stage
    VERIFY_ANSWER = 'verify_answer'  # Verify the answer

class Subjects:
    # SUBJECTS POSSIBLES
    GENERAL_CONTACT = 'general_contact'
    HIRE_US = 'hire_us'
    JOIN_THE_TEAM = 'join_the_team'
              
class Paths:
    ASSESTS_PATH = 'Backend/Application/KobuAssistant/Storage/assets'
    # ASSISTANT BUFFER PATHS
    BUFFER_SAVER_FILE_PATH = ASSESTS_PATH + '/buffer/buffer.json'
    EXPOERTED_LEAD_DATAS = ASSESTS_PATH + '/buffer/lead_datas.json'
    # KNWOLEDGE PATHS
    BASIC_INSTRUCTIONS_PATH =  ASSESTS_PATH + '/basic_instructions.json'
    DATA_REQUIRED_PATH: str = ASSESTS_PATH + '/{subject_name}/{subject_name}_data_required.txt'
    ASSISTANT_INSTRUCTIONS_PATH: str = ASSESTS_PATH + '/{subject_name}/{self.subject_name}_instructions.json'
    FUNCTION_DESCRIPTION_PATH = ASSESTS_PATH + '/{subject_name}/{subject_name}_function_description.json'
    WEB_SCRAPER_FILES_PATH = ASSESTS_PATH + 'Storage/assets/web_scraper_files'
class ChatConsts(Stages, FlowOrientations, Subjects, Paths):
    pass
