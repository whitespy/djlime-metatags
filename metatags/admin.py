from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import MetaTag
from .forms import InlineMetaTagForm, MetaTagForm


class MetaTagInline(generic.GenericStackedInline):
    model = MetaTag
    extra = 1
    max_num = 1
    form = InlineMetaTagForm


class MetaTagAdmin(admin.ModelAdmin):
    form = MetaTagForm
    list_display = ('url',)

    def queryset(self, request):
        qs = super(MetaTagAdmin, self).queryset(request)
        return qs.filter(content_type__isnull=True, object_id__isnull=True)

admin.site.register(MetaTag, MetaTagAdmin)
