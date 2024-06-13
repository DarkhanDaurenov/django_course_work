from django.core.mail import send_mail
from .models import Distribution, TryLetter
from datetime import datetime
import smtplib

def send_mails():
    now = datetime.now()
    distributions = Distribution.objects.filter(start_time__lte=now, status=Distribution.CREATE)

    for distribution in distributions:
        clients = distribution.clients.all()
        letter = distribution.message

        for client in clients:
            try:
                send_mail(
                    letter.title_message,
                    letter.body_message,
                    'from@example.com',
                    [client.email],
                    fail_silently=False,
                )
                print(f"Письмо отправленно на  {client.email} with subject: {letter.title_message}")
                TryLetter.objects.create(
                    distribution=distribution,
                    try_start_time=now,
                    try_status=TryLetter.SUCCESS,
                    mail_answer='Email successfully sent to ' + client.email
                )
            except smtplib.SMTPException as e:
                print(f"Письмо не отправленно {client.email}: {e}")
                TryLetter.objects.create(
                    distribution=distribution,
                    try_start_time=now,
                    try_status=TryLetter.UNSUCCESSFUL,
                    mail_answer=str(e)
                )
            except Exception as e:
                print(f"Ошибка отправки письма {client.email}: {e}")
                TryLetter.objects.create(
                    distribution=distribution,
                    try_start_time=now,
                    try_status=TryLetter.UNSUCCESSFUL,
                    mail_answer=str(e)
                )