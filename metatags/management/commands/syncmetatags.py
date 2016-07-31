from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, **options):
        if 'modeltranslation' in settings.INSTALLED_APPS:
            try:
                call_command('sync_translation_fields', interactive=False)
                call_command('update_translation_fields')
            except CommandError:
                self.stderr.write('Unknown error.')
            else:
                self.stdout.write('Fields have been successfully synchronized.')
        else:
            self.stderr.write('django-modeltranslation is not installed.')
