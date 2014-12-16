from django.conf import settings


def add_translation_tabs_inline(cls):
    if 'modeltranslation' in settings.INSTALLED_APPS:
        from modeltranslation.admin import TranslationGenericStackedInline

        cls.__bases__ = (TranslationGenericStackedInline,)

    return cls


def add_translation_tabs(cls):
    if 'modeltranslation' in settings.INSTALLED_APPS:
        from modeltranslation.admin import TranslationAdmin

        class Media:
            js = (
                'modeltranslation/js/force_jquery.js',
                'js/jquery-ui.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',)
            }

        cls.__bases__ = (TranslationAdmin,)
        cls.Media = Media

    return cls
