from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
import json
import os

os.environ["OPENAI_API_KEY"] = "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"
# load_dotenv()
# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

class LeadExtractor():
    """Class for extracting lead data from conversation."""
    CLIENT = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    TEMPERATURE = 0.6
    MODEL = "gpt-3.5-turbo"

    def __init__(self):
        self.function_description_path = 'function_description.json'
        self.files_tree_path = 'scraper_files_tree.json'

        with open(self.function_description_path, 'r', encoding='utf-8') as json_file:
            self.function_description = json.load(json_file)

        with open(self.files_tree_path, 'r', encoding='utf-8') as json_file:
            self.files_tree = json.load(json_file)

    def main(self, file_path='dossier_biography_structure.json'):
        """Extract and save lead data."""
        function_arguments = self.extract_data()
        self.save_json_to_file(function_arguments, file_path)

    def extract_data(self, tool_choice='auto'):
        """Extracts data from chat history using GPT-3."""
        functions_descriptions = [{
            "name": "BibliographyOrganizer",
            "description": self.function_description.get('description'),
            "parameters": self.function_description.get('parameters')
        }]
        print("Lead Extractor - extract_datas(): Extracting data to generate lead...")

        try:
            completion = self.CLIENT.chat.completions.create(
                model=self.MODEL,  # Este modelo é melhor para extrações
                temperature=self.TEMPERATURE,
                messages=[
                    {'role': 'system',
                     'content': 'Você é um assistente que organiza bibliografias com base na árvore de diretórios fornecida.'},
                    {'role': 'system',
                     'content': 'Seu trabalho é associar cada tópico aos arquivos mais relevantes no diretório.'},
                    {'role': 'system',
                     'content': 'Se a árvore de arquivos contiver todos os dados necessários, extraia esses dados e organize-os em um JSON.'},
                    {'role': 'system',
                     'content': 'Assegure-se de associar cada arquivo ao argumento mais relevante conforme descrito.'},
                    {'role': 'user', 'content': f"Árvore de arquivos: {json.dumps(self.files_tree, ensure_ascii=False)}"}
                ],
                functions=functions_descriptions,
                function_call=tool_choice
            )

            print("Lead Extractor - extract_datas(): Enough data to generate lead")

            output = completion.choices[0].message
            print(output)
            arguments = output.function_call.arguments
            arguments_dict = json.loads(arguments)

            # tool_calls = output['function_call']
            # tool_call_arguments = tool_calls['arguments']
            # function_arguments = json.loads(tool_calls)

            print(arguments_dict)
            return arguments_dict

        except Exception as e:
            print(f"Error extracting data: {e}")
            return {}

    def save_json_to_file(self, data, file_path):
        """
        Salva o dicionário fornecido em um arquivo JSON no caminho especificado.

        :param data: O dicionário a ser salvo.
        :param file_path: O caminho do arquivo onde o JSON será salvo.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            print(f"JSON salvo com sucesso em {file_path}")
        except Exception as e:
            print(f"Erro ao salvar JSON: {e}")

lead = LeadExtractor()
lead.main()
