import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass  

def enviar_email_assistencia(pergunta_usuario, email_usuario, email_empresa):
   
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL = ""#email
    SENHA = ""  #senha específica de app  

    
    
    if "@" not in email_empresa or "." not in email_empresa.split("@")[1]:
        print("Erro: E-mail da empresa inválido")
        return False

    try:
        
        mensagem = MIMEMultipart()
        mensagem['From'] = EMAIL
        mensagem['To'] = email_empresa
        mensagem['Subject'] = f"Dúvida de {email_usuario}"
        mensagem['Reply-To'] = email_usuario

        corpo = f"""
        Nova dúvida recebida:

        Cliente: {email_usuario}
        Pergunta: {pergunta_usuario}

        Por favor, responda diretamente ao cliente.
        """
        mensagem.attach(MIMEText(corpo, 'plain'))

        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10) as server:
            server.ehlo()
            server.starttls()
            server.login(EMAIL, SENHA)
            server.send_message(mensagem)
            print(f"E-mail enviado para {email_empresa}")
        
        return True

    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação. Verifique:")
        print("- Se a App Password está correta (sem espaços)")
        print("- Se a verificação em duas etapas está ativada")
        print("- Se você permitiu 'Acesso a app menos seguro'")
        return False
        
    except Exception as e:
        print(f"Erro no envio: {str(e)}")
        return False