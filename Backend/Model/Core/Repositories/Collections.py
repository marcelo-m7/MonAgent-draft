from langchain_openai import ChatOpenAI
from Backend.Application.Core.Utils.VectorStoreBuilder import get_vector_store
from langchain_community.vectorstores.faiss import VectorStore

llm_conversation: ChatOpenAI = ChatOpenAI(temperature=1, model="gpt-3.5-turbo")
llm_validation: ChatOpenAI = ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo")
llm_retriver: ChatOpenAI = ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo")
vector_store: VectorStore = get_vector_store(json_folder="Backend\Application\KobuAssistant\Storage\assets")
