from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        if 'modeltranslation' in settings.INSTALLED_APPS:
            try:
                call_command('sync_translation_fields')
                call_command('update_translation_fields')
            except CommandError:
                self.stderr.write('Unknown error')
            else:
                self.stdout.write('Fields successfully synchronized')
        else:
            self.stderr.write('django-modeltranslation not installed')
