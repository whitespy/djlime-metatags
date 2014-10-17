from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MetaTagsConfig(AppConfig):
    name = 'metatags'
    verbose_name = _('Meta tags')
