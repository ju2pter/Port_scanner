import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()

def enviar_email(remetente, senha, destinatario, assunto, mensagem, anexo=None):
    """
    Envia um e-mail com ou sem anexo.
    
    Args:
        remetente (str): Endereço de e-mail do remetente.
        senha (str): Senha do e-mail do remetente.
        destinatario (str): Endereço de e-mail do destinatário.
        assunto (str): Assunto do e-mail.
        mensagem (str): Corpo da mensagem.
        anexo (str, opcional): Caminho do arquivo a ser anexado. Padrão é None.
    """
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)

        email = MIMEMultipart()
        email['From'] = remetente
        email['To'] = destinatario
        email['Subject'] = assunto
        email.attach(MIMEText(mensagem, 'plain'))

        if anexo:
            nome_arquivo = os.path.basename(anexo)
            with open(anexo, 'rb') as arquivo:
                parte_anexo = MIMEBase('application', 'octet-stream')
                parte_anexo.set_payload(arquivo.read())
            encoders.encode_base64(parte_anexo)
            parte_anexo.add_header(
                'Content-Disposition',
                f'attachment; filename={nome_arquivo}'
            )
            email.attach(parte_anexo)

        servidor.sendmail(remetente, destinatario, email.as_string())
        servidor.quit()

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")


if __name__ == "__main__":
    remetente = os.getenv("EMAIL_USER")
    senha = os.getenv("EMAIL_PASS")
    destinatario = input("Digite o e-mail do destinatário: ")
    assunto = input("Digite o assunto: ")
    mensagem = input("Digite a mensagem: ")
    anexo = input("Digite o caminho do anexo (ou pressione Enter para ignorar): ").strip() or None

    if not remetente or not senha:
        print("Erro: configure as variáveis de ambiente EMAIL_USER e EMAIL_PASS.")
    else:
        enviar_email(remetente, senha, destinatario, assunto, mensagem, anexo)
