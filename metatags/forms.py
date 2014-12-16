import re

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .models import MetaTag


url_re = re.compile(r'^(?P<url_path>[-\w/\.~]+)(?:/?|[/?]\S+)$', re.IGNORECASE)


class InlineMetaTagForm(forms.ModelForm):

    class Meta:
        fields = ('title', 'keywords', 'description')

    class Media:
        css = {
            'all': ('css/meta_tags.css',)
        }


class MetaTagForm(InlineMetaTagForm):
    url = forms.RegexField(label=_('URL-path'), max_length=100, regex=url_re,
                           help_text=_("Example: '/about/contact/'. Make sure to have leading "
                                       "and trailing slashes."),
                           error_message=_("This value must contain only letters, numbers,"
                                           "dots, underscores, dashes, slashes or tildes."))

    class Meta:
        fields = ('url', 'title', 'keywords', 'description')

    def clean_url(self):
        url = self.cleaned_data['url']

        if not url.startswith('/'):
            raise forms.ValidationError(_('URL is missing a leading slash.'))

        if settings.APPEND_SLASH and 'django.middleware.common.CommonMiddleware' in settings.MIDDLEWARE_CLASSES:
            url_match = url_re.match(url)
            url_path = url_match.group('url_path')

            if not url_path.endswith('/'):
                raise forms.ValidationError(_('URL is missing a trailing slash.'))

        if MetaTag.objects.filter(url=url).exists():
            if self.instance is None or url != self.instance.url:
                raise forms.ValidationError(_('Meta-tags for a given URL-path have already been identified.'))

        return url
