🤖 Agente de Suporte NowGo IA

Este é um chatbot inteligente feito em Python que oferece suporte técnico automatizado. Ele responde dúvidas com base em um FAQ interno e, se necessário, consulta uma inteligência artificial. Caso não consiga responder, encaminha a dúvida por e-mail para a equipe de suporte.


🚀 Funcionalidades

- 🔎 Busca por respostas em um arquivo de FAQ (`faq.json`)
- 🧠 Consulta a um modelo de linguagem natural (LLM) via Hugging Face
- 📩 Encaminhamento automático de dúvidas não respondidas via e-mail
- 💬 Interface simples via terminal
  

🗂️ Estrutura dos arquivos
```
├── agente.py - Script principal do chatbot
├── email_sender.py - Função para enviar dúvidas por e-mail
├── faq.json - Base de perguntas e respostas frequentes (FAQ)
├── faq.py - Leitura do FAQ (não usado diretamente no agente)
├── faq_manager.py - Funções para carregar e buscar respostas no FAQ
├── llm.py - Integração com modelo LLM (Mistral-7B-Instruct via HuggingFace)
```


🧠 Como funciona

1. O usuário digita sua pergunta.
2. O sistema tenta encontrar a resposta no FAQ local.
3. Caso não encontre, envia a pergunta para um modelo LLM.
4. Se a IA também não souber responder, o usuário é solicitado a informar um e-mail para que a dúvida seja encaminhada à equipe.

🛠️ Requisitos

- Python 3.8+
- Conta na HuggingFace com o modelo [`mistralai/Mistral-7B-Instruct`](https://huggingface.co/mistralai/Mistral-7B-Instruct)
- Uma conta de e-mail configurada para envio SMTP (ex: Gmail com senha de app)

