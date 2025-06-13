import json

def carregar_faq():
    try:
        with open("faq.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def buscar_resposta_faq(pergunta, faq):
    pergunta_lower = pergunta.lower()
    for chave, resposta in faq.items():
        if pergunta_lower in chave.lower():
            return resposta
    return None