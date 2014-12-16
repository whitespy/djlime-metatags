from django.template import Library
from django.shortcuts import _get_queryset
from django.utils.encoding import force_text

from metatags.models import MetaTag
from metatags.utils import truncate_language_code


register = Library()


def _get_page_title(page_object, page_title_field):
    return getattr(page_object, page_title_field, force_text(page_object))


def _get_object_or_none(cls, *args, **kwargs):
    queryset = _get_queryset(cls)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None


@register.inclusion_tag('metatags/_meta_tags.html', takes_context=True)
def include_meta_tags(context, page_object=None, page_title_field='title',
                      default_title='', default_keywords='', default_description=''):
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
            meta_tags.keywords = meta_tags.keywords or default_keywords
            meta_tags.description = meta_tags.description or default_description
        except MetaTag.DoesNotExist:
            meta_tags = {
                'title': _get_page_title(page_object, page_title_field),
                'keywords': default_keywords,
                'description': default_description
            }
    else:
        # Get the meta tags for the URL-path
        try:
            full_url_path = truncate_language_code(context['request'].get_full_path())
            meta_tags = _get_object_or_none(MetaTag, url=full_url_path)

            if meta_tags is None:
                url_path = truncate_language_code(context['request'].path_info)
                meta_tags = MetaTag.objects.get(url=url_path)

            meta_tags.title = meta_tags.title or default_title
            meta_tags.keywords = meta_tags.keywords or default_keywords
            meta_tags.description = meta_tags.description or default_description
        except (KeyError, MetaTag.DoesNotExist):
            meta_tags = {
                'title': default_title,
                'keywords': default_keywords,
                'description': default_description
            }
    return {'meta_tags': meta_tags}
