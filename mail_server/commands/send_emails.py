from django.core.management.base import BaseCommand
from mail_server.utils import send_emails

class Command(BaseCommand):
    help = 'Send emails for active distributions'

    def handle(self, *args, **options):
        send_emails()
        self.stdout.write(self.style.SUCCESS('Successfully sent emails'))