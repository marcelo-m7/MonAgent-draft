from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.runnables import Runnable
from Core.Utils.LeadExtractor import LeadExtractor, Lead
from Repositories.prompts import Prompts
from Repositories.enviroments import ConversationEnviroment
from Repositories.collections import *
import json
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

class Utils:
    buffer_saver_file_path = p.BUFFER_SAVER_FILE_PATH
    exported_lead_datas = p.EXPOERTED_LEAD_DATAS

    async def conversation_buffer(self, cv: ConversationEnviroment,
                                  user_input: bool = False, 
                                  assistant_response_message: bool = False, 
                                  system_message: str = None) -> None:
        try: 
            
            if user_input:
                cv.conversation_history.append(HumanMessage(content=cv.user_input))

            if assistant_response_message:
                cv.conversation_history.append(AIMessage(content=cv.assistant_response_message))
                cv.conversation_history.append(SystemMessage(content=f"Awnswered at: {datetime.now()}"))

            if system_message:
                cv.conversation_history.append(SystemMessage(content=f"{system_message}\nSystem Message set at: {datetime.now()}"))
                
            print("Buffer saved in cv.conversation_history list")

        except Exception as e:
            print(f"chat_buffer Error {e}")
    
    async def conversation_buffer_local(self, user_input: str, response: str) -> None:
        """
        Save the chat history in a JSON file.
        
        Args:
            user_input (str): User input message.
            response (str): Assistant response message.
        """

        messages_history = []
        messages_history.append({'role': 'user', 'content': user_input})
        messages_history.append({'role': 'assistant', 'content': response})
        messages_history.append({'role': 'system', 'content': datetime.now()})
        try:
            try:
                with open(self.buffer_saver_file_path, 'r', encoding='utf-8') as existing_json_file:
                    existing_data = json.load(existing_json_file)
            except FileNotFoundError:
                existing_data = []

            existing_data.extend(messages_history)
            with open(self.buffer_saver_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=2)

            print(f'cv.conversation_history saved in {self.buffer_saver_file_path}')
        except Exception as e:
            print(f"chat_buffer_saver Error {e}")

    async def obtain_assistant_message_response(self, cv: ConversationEnviroment):
        prompt = Prompts(cv=cv)
        prompt_inputs = prompt.prompt_references
        llm = llm_conversation
        chain = prompt.prompt() | llm

        if cv.extra_context_flag:
            chain = create_stuff_documents_chain(
                llm=llm_conversation,
                prompt=prompt
            )
            retriever = vector_store.as_retriever(search_kwargs={"k": cv.search_kwargs})
            retriever_prompt = prompt.retriever_prompt()
            history_aware_retriever = create_history_aware_retriever(
                llm=llm_retriver,
                retriever=retriever,
                prompt=retriever_prompt
            )
            retrieval_chain = create_retrieval_chain(
                retriever,
                history_aware_retriever,
                chain
            )
            chain: Runnable = retrieval_chain | prompt | llm_conversation 

        reponse = await chain.invoke(dict(prompt_inputs))
        print("Assistant response:\n", reponse)
        return reponse
    
    async def extract_lead_from_conversation(self, cv: ConversationEnviroment) -> Lead:
        lead_extractor = LeadExtractor(subject_name=cv.conversation_subject)
        return await lead_extractor.extract_lead(cv.conversation_history)

   