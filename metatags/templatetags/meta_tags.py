from django.template import Library
from django.utils.encoding import force_unicode

from metatags.models import MetaTag


register = Library()

_get_page_title = lambda page_object, page_title_field: (
    getattr(page_object, page_title_field, force_unicode(page_object))
)


@register.inclusion_tag('metatags/meta_tags.html', takes_context=True)
def include_meta_tags(context, page_object=None, page_title_field='title'):
    if page_object is not None:
        # Get the meta tags for the object
        try:
            meta_tags = MetaTag.objects \
                .get(object_id=page_object.id,
                     content_type__app_label=page_object._meta.app_label,
                     content_type__model=page_object._meta.module_name)
            # Get not blank title
            meta_tags.title = meta_tags.title or \
                _get_page_title(page_object, page_title_field)
        except MetaTag.DoesNotExist:
            meta_tags = {
                'title': _get_page_title(page_object, page_title_field)
            }
    else:
        # Get the meta tags for the URL-path
        url_path = context['request'].path_info
        try:
            meta_tags = MetaTag.objects.get(url=url_path)
            # Get not blank title
            meta_tags.title = meta_tags.title or \
                _get_page_title(page_object, page_title_field)
        except MetaTag.DoesNotExist:
            meta_tags = None

    return {'meta_tags': meta_tags}
