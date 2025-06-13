from huggingface_hub import InferenceClient

client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.3")

def perguntar_para_llm(pergunta):
    try:
        resposta = client.text_generation(
            prompt=f"Você é um assistente técnico. Responda de forma clara e concisa:\n{pergunta}",
            max_new_tokens=200,
            temperature=0.7
        )
        return resposta.strip()
    except Exception as e:
        return f"Erro: {str(e)}"