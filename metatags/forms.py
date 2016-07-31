from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .models import MetaTag


class InlineMetaTagForm(forms.ModelForm):

    class Meta:
        fields = ('title', 'keywords', 'description')

    @property
    def media(self):
        _media = forms.Media(css={'all': ('css/meta_tags.css',)})
        if 'modeltranslation' in settings.INSTALLED_APPS:
            _media.add_css({'all': ('modeltranslation/css/tabbed_translation_fields.css',)})
            _media.add_js(('modeltranslation/js/force_jquery.js', 'js/jquery-ui.min.js',
                           'modeltranslation/js/tabbed_translation_fields.js'))
        return _media


class MetaTagForm(InlineMetaTagForm):
    url = forms.RegexField(label=_('URL-path'), max_length=100, regex=r'^[-\w/\.~]+$',
                           help_text=_("Example: '/about/contact/'. Make sure to have leading and trailing slashes."),
                           error_messages={'invalid': _("This value must contain only letters, numbers, dots, "
                                                        "underscores, dashes, slashes or tildes.")})

    class Meta:
        fields = ('url', 'title', 'keywords', 'description')

    def clean_url(self):
        url = self.cleaned_data['url']

        if not url.startswith('/'):
            raise forms.ValidationError(_('URL is missing a leading slash.'))

        if (not url.endswith('/') and settings.APPEND_SLASH and
                'django.middleware.common.CommonMiddleware' in settings.MIDDLEWARE_CLASSES):
            raise forms.ValidationError(_('URL is missing a trailing slash.'))

        if MetaTag.objects.filter(url=url).exists():
            if self.instance is None or url != self.instance.url:
                raise forms.ValidationError(_('Meta tags for a given URL-path have already been identified.'))

        return url
