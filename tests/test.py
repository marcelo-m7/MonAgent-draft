import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')
from VectorStoreBuilder import get_document_store

class CompanyAssistant:
    def __init__(self, company_website):
        self.company_website = company_website
        self.document_content = self.retrieve_document_content()
        self.document_sentences = self.tokenize_sentences(self.document_content)
        self.sentence_embeddings = self.generate_sentence_embeddings(self.document_sentences)

    def retrieve_document_content(self):
        # # Function to retrieve document content from the company website
        # response = requests.get(self.company_website)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # # Extract document content from HTML elements
        # document_content_element = soup.find('div')
        # if document_content_element:
        #     document_content = document_content_element.text
        # else:
        #     print(document_content)
        #     document_content = "Failed to retrieve document content"
        document_content = str(get_document_store())
        return document_content

    def tokenize_sentences(self, text):
        # Tokenize document content into sentences
        return sent_tokenize(text)

    def generate_sentence_embeddings(self, sentences):
        # Generate embeddings for each sentence in the document
        model = SentenceTransformer('bert-base-nli-mean-tokens')
        sentence_embeddings = model.encode(sentences)
        return sentence_embeddings

    def find_most_similar_sentence(self, user_input):
        # Compute similarity between user input and document sentences
        user_input_embedding = self.generate_sentence_embeddings([user_input])[0]
        similarities = cosine_similarity([user_input_embedding], self.sentence_embeddings)[0]
        most_similar_sentence_index = similarities.argmax()
        most_similar_sentence = self.document_sentences[most_similar_sentence_index]
        return most_similar_sentence

# Example usage:
if __name__ == "__main__":
    company_website = 'https://kobu.agency/agency'
    assistant = CompanyAssistant(company_website)

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        else:
            response = assistant.find_most_similar_sentence(user_input)
            print("Assistant:", response)
