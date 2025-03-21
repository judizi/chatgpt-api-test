import re


def delete_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def modify_answer(text: str):
    return text.strip()


def make_prompt(content):
    prompt = f'''{delete_spaces(content)}'''.strip()
    return prompt

def print_pretty(text):
    print("-"*50)
    print(str(text))
    print("-"*50)

def print_result(prompt, result):
    print("#"*50)
    print("-> 질의")
    print_pretty(prompt)
    print("-> 응답")
    print_pretty(result)
    print("#"*50)
    