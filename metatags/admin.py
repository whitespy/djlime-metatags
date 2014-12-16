from django.contrib import admin

try:
    from django.contrib.contenttypes.admin import GenericStackedInline
except ImportError:
    from django.contrib.contenttypes.generic import GenericStackedInline

from .models import MetaTag
from .forms import InlineMetaTagForm, MetaTagForm
from .decorators import add_translation_tabs_inline, add_translation_tabs


@add_translation_tabs_inline
class MetaTagInline(GenericStackedInline):
    model = MetaTag
    extra = 1
    max_num = 1
    form = InlineMetaTagForm
    template = 'metatags/edit_inline/stacked.html'


@add_translation_tabs
class MetaTagAdmin(admin.ModelAdmin):
    form = MetaTagForm
    list_display = ('url',)
    search_fields = ['url', 'title', 'keywords', 'description']

    def get_queryset(self, request):
        qs = super(MetaTagAdmin, self).get_queryset(request)
        return qs.filter(content_type__isnull=True, object_id__isnull=True)

admin.site.register(MetaTag, MetaTagAdmin)
