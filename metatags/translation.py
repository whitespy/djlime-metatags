from modeltranslation.translator import translator, TranslationOptions

from .models import MetaTag


class MetaTagTranslationOptions(TranslationOptions):
    fields = ('title', 'keywords', 'description')

translator.register(MetaTag, MetaTagTranslationOptions)
