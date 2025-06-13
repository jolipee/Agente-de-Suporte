import json

def carregar_faq():
    with open("faq.json", "r", encoding="utf-8") as f:
        return json.load(f)
