# app_gradio.py  – coloque na raiz do projeto

import re
import gradio as gr
from faq_manager import carregar_faq, buscar_resposta_faq          # seu código :contentReference[oaicite:0]{index=0}
from llm import perguntar_para_llm                                # seu código :contentReference[oaicite:1]{index=1}
from email_sender import enviar_email_assistencia                 # seu código :contentReference[oaicite:2]{index=2}

# --- Configurações ---
FAQ = carregar_faq()                     # carrega faq.json uma vez
DESTINO_EMPRESA = "joaofilipealvess@gmail.com"   # e‑mail que recebe as dúvidas
EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

# Variável global simples para lembrar a pergunta que ficou sem resposta
pendente = None

# --- Função chamada pelo ChatInterface ---
def responder(mensagem: str, historico):
    """
    Fluxo:
      1. Se o bot pediu e-mail, qualquer texto que bata com regex é tratado como e‑mail.
      2. Caso normal: FAQ → LLM → pede e‑mail se falhar.
    Retorna UM dicionário 'role/content', que o ChatInterface adiciona ao histórico.
    """
    global pendente

    # 1) O usuário acabou de fornecer e-mail?
    if pendente and EMAIL_RE.fullmatch(mensagem.strip()):
        enviar_email_assistencia(pendente, mensagem.strip(), DESTINO_EMPRESA)
        pendente = None
        return {"role": "assistant",
                "content": "✅ Obrigado! Sua dúvida foi encaminhada à equipe."}

    # 2) Tenta FAQ
    resposta = buscar_resposta_faq(mensagem, FAQ)
    if resposta:
        return {"role": "assistant", "content": resposta}

    # 3) Tenta LLM
    resposta = perguntar_para_llm(mensagem)
    if not resposta or resposta.lower().startswith("erro"):
        pendente = mensagem      
        return {"role": "assistant",
                "content": (
                    "Não encontrei a resposta agora 🤖.\n"
                    "Por favor, digite seu e‑mail para que nossa equipe entre em contato:"
                )}

    return {"role": "assistant", "content": resposta}

chatbot = gr.Chatbot(type="messages", height=460)

demo = gr.ChatInterface(
    fn=responder,
    chatbot=chatbot,
    title="Bia • Suporte Técnico",
    theme="soft",
)

if __name__ == "__main__":
    demo.launch(server_port=7860, share=False)   # abra http://127.0.0.1:7860
