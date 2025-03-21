from openai import OpenAI

from utils.formatter import make_prompt, modify_answer, print_result
from utils.load_file import load_key, load_question

OPENAI_MODEL = "gpt-4o-mini"


class ChatGPT:
    def __init__(self, openai_organization, openai_api_key, openai_model):
        self.client = OpenAI(
            organization=openai_organization,
            api_key=openai_api_key,
        )
        self.openai_model = openai_model


    def ask_question(self, prompt):
        try:
            response = self.client.chat.completions.create(
                            model=self.openai_model,
                            messages=[
                                        {
                                            "role": "user",
                                            "content": [
                                                {"type": "text", "text": prompt}
                                            ]
                                        }
                                    ]
                                )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return str(e)


if __name__ == "__main__":
    key_data = load_key()
    if key_data is None:
        print("error :: key is not exist")
    else:
        chat_gpt = ChatGPT(key_data['OPENAI_ORGANIZATION'], key_data['OPENAI_API_KEY'], OPENAI_MODEL)
        
        contents_list = load_question()
        for contents_text in contents_list:
            prompt = make_prompt(contents_text)
            result = modify_answer(chat_gpt.ask_question(prompt))
            print_result(prompt, result)
