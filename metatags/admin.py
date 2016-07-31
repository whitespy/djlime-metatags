from django import forms
from django.utils import six
from django.contrib import admin
from django.conf import settings
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import MetaTag
from .forms import InlineMetaTagForm, MetaTagForm


class MetaTagInlineMeta(forms.MediaDefiningClass):

    def __new__(mcs, name, bases, attrs):
        if 'modeltranslation' in settings.INSTALLED_APPS:
            from modeltranslation.admin import TranslationGenericStackedInline
            bases = (TranslationGenericStackedInline,)
        return super(MetaTagInlineMeta, mcs).__new__(mcs, name, bases, attrs)


class MetaTagAdminMeta(forms.MediaDefiningClass):

    def __new__(mcs, name, bases, attrs):
        if 'modeltranslation' in settings.INSTALLED_APPS:
            from modeltranslation.admin import TranslationAdmin
            bases = (TranslationAdmin,)
        return super(MetaTagAdminMeta, mcs).__new__(mcs, name, bases, attrs)


class MetaTagInline(six.with_metaclass(MetaTagInlineMeta, GenericStackedInline)):
    model = MetaTag
    extra = 1
    max_num = 1
    can_delete = False
    form = InlineMetaTagForm
    template = 'metatags/admin/edit_inline/stacked.html'


@admin.register(MetaTag)
class MetaTagAdmin(six.with_metaclass(MetaTagAdminMeta, admin.ModelAdmin)):
    form = MetaTagForm
    list_display = ('url',)
    search_fields = ['url', 'title', 'keywords', 'description']

    def get_queryset(self, request):
        return super(MetaTagAdmin, self).get_queryset(request).filter(
            content_type__isnull=True, object_id__isnull=True)
