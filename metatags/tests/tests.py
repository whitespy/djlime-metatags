from django.test import SimpleTestCase
from django.test.utils import override_settings

from metatags.utils import truncate_language_code


_LANGUAGES = (
    ('ru', 'Russian'),
    ('uk', 'Ukrainian'),
    ('en', 'English')
)


@override_settings(LANGUAGES=_LANGUAGES)
class TestMetaTags(SimpleTestCase):

    def test_truncate_language_code(self):
        self.assertEqual(truncate_language_code('/en/'), '/',
                         'Incorrect truncation a /en/ path')

        self.assertEqual(truncate_language_code('/en/services/'), '/services/',
                         'Incorrect truncation a /en/services/ path')

        self.assertEqual(truncate_language_code('/end/'), '/end/',
                         'Incorrect truncation a /end/ path')