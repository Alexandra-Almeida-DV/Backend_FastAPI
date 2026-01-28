import smtplib
from email.mime.text import MIMEText
from app.core.config import settings

def send_contact_email(data):
    site_emails = settings.site_emails()

    if data.site_id not in site_emails:
        raise ValueError("Site não configurado")

    to_email = site_emails[data.site_id]

    body = f"""
Site: {data.site_id}

Nome: {data.nome}
Email: {data.email}

Mensagem:
{data.mensagem}
    """

    msg = MIMEText(body)
    msg["Subject"] = f"Novo contato - {data.site_id}"
    msg["From"] = settings.email_user
    msg["To"] = to_email

    with smtplib.SMTP_SSL(settings.email_host, settings.email_port) as server:
        server.login(settings.email_user, settings.email_pass)
        server.send_message(msg)
