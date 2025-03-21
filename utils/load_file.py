import json


def load_key():
    key_data = None
    try:
        with open("./openai_key.json", "r", encoding="utf-8") as file:
            key_data = json.load(file)
    except Exception as e:
        print("error :: " + str(e))

    return key_data

def load_question():
    questions = []
    try:
        with open("./data/questions.txt", "r", encoding="utf-8") as file:
            for line in file:
                questions.append(line.strip())
    except Exception as e:
        print("error :: " + str(e))
    finally:
        return questions