import logging

from django.core.management.base import BaseCommand

from django_mailbox.models import Mailbox


class Command(BaseCommand):
    args = "<[PullDays (optional)]>"

    def add_arguments(self, parser):
        parser.add_argument(
            '--pull_days',
            nargs='?',
            type=int,
            help="The number of days to pull messages from"
        )

    def handle(self, pull_days=None, *args, **options):
        logging.basicConfig(level=logging.INFO)
        Mailbox.get_new_mail_all_mailboxes(args, pull_days)
