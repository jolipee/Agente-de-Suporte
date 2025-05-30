from faq_manager import carregar_faq, buscar_resposta_faq
from llm import perguntar_para_llm
from email_sender import enviar_email_assistencia

def main():
    faq = carregar_faq()
    print("=== Agente de Suporte Técnico ===")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        pergunta = input("Digite sua dúvida: ").strip()
        if pergunta.lower() == "sair":
            break
        
        resposta_faq = buscar_resposta_faq(pergunta, faq)
        if resposta_faq:
            print("\nBia (BOT):", resposta_faq)
        else:
            print("\nAgente: Não encontrei no FAQ. Buscando resposta inteligente...")
            resposta_llm = perguntar_para_llm(pergunta)
            
            if "Erro" in resposta_llm or not resposta_llm:
                print("\nAgente: Não consegui responder. Vou encaminhar para nossa equipe.")
                email_usuario = input("Por favor, digite seu e-mail para que possamos entrar em contato: ").strip()
                
                if "@" in email_usuario:  
                    sucesso = enviar_email_assistencia(pergunta, email_usuario, "") #email
                    if sucesso:
                        print("\nObrigado! Sua dúvida foi encaminhada e entraremos em contato em breve.")
                    else:
                        print("\nHouve um erro ao enviar sua dúvida. Por favor, tente novamente mais tarde.")
                else:
                    print("\nE-mail inválido. Não foi possível encaminhar sua dúvida.")
            else:
                print("\nAgente (IA):", resposta_llm)

if __name__ == "__main__":
    main()