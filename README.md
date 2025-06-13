
 Agente de Suporte Autônomo 

Este projeto é um agente de suporte inteligente feito pra Nowgo IA que responde dúvidas de clientes com base em um FAQ, complementado por uma IA generativa. Quando a IA não consegue ajudar, ele solicita o e‑mail do usuário e envia a dúvida automaticamente para a equipe de atendimento.

---

## ✨ Funcionalidades

- 🔎 Responde perguntas com base em um FAQ (`faq.json`)
- 💬 Usa LLM (modelo de linguagem) para responder perguntas abertas
- 📧 Solicita e‑mail caso a IA não saiba responder
- 📤 Encaminha a dúvida para o time de suporte automaticamente
- 🌐 Interface web com Gradio (sem precisar do terminal)

---

## 📁 Estrutura do Projeto

```bash
agenteSuporte/
├── app_gradio.py          # Interface principal com Gradio
├── email_sender.py        # Função de envio de e‑mails
├── faq.json               # Arquivo com perguntas e respostas frequentes
├── faq.py                 # (opcional - auxiliar para o FAQ)
├── faq_manager.py         # Funções para carregar e consultar o FAQ
├── llm.py                 # Integração com modelo de linguagem (IA)
├── README.md              # Este arquivo
