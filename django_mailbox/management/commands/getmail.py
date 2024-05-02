import logging

from django.core.management.base import BaseCommand

from django_mailbox.models import Mailbox


class Command(BaseCommand):
    args = "<[PullDays (optional)]>"

    def add_arguments(self, parser):
        parser.add_argument(
            'pull_days',
            nargs='?',
            help="The name of the mailbox that will receive the message"
        )

    def handle(self, pull_days=None, *args, **options):
        logging.basicConfig(level=logging.INFO)
        Mailbox.get_new_mail_all_mailboxes(args, pull_days)
