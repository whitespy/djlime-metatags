from django.test import TestCase
from django.contrib.auth import get_user_model

from metatags.utils import truncate_language_code


class DjangoDummyHttpRequest(object):

    def __init__(self, path_info):
        self.path_info = path_info


class TestMetaTags(TestCase):

    def test_truncate_language_code(self):
        self.assertEqual(truncate_language_code('/en/'), '/')
        self.assertEqual(truncate_language_code('/end/'), '/end/')
        self.assertEqual(truncate_language_code('/en/services/'), '/services/')

    def test_get_meta_tags_for_object(self):
        from metatags.models import MetaTag
        from metatags.templatetags.meta_tags import include_meta_tags

        UserModel = get_user_model()
        test_user = UserModel.objects.create(username='test_user')
        meta_tag_model_instance = MetaTag.objects.create(title='test user title', keywords='test user keywords',
                                                         description='test user description', content_object=test_user)
        meta_tag_template_context_dict = include_meta_tags({}, test_user)
        self.assertEqual(meta_tag_model_instance.title, meta_tag_template_context_dict['meta_tags'].title)
        self.assertEqual(meta_tag_model_instance.keywords, meta_tag_template_context_dict['meta_tags'].keywords)
        self.assertEqual(meta_tag_model_instance.description, meta_tag_template_context_dict['meta_tags'].description)

    def test_get_meta_tags_by_url_path(self):
        from metatags.models import MetaTag
        from metatags.templatetags.meta_tags import include_meta_tags

        request = DjangoDummyHttpRequest('/foo/bar/')
        meta_tag_model_instance = MetaTag.objects.create(url=request.path_info, title='test title',
                                                         keywords='test keywords', description='test description')
        meta_tag_template_context_dict = include_meta_tags({'request': request})
        self.assertEqual(meta_tag_model_instance.title, meta_tag_template_context_dict['meta_tags'].title)
        self.assertEqual(meta_tag_model_instance.keywords, meta_tag_template_context_dict['meta_tags'].keywords)
        self.assertEqual(meta_tag_model_instance.description, meta_tag_template_context_dict['meta_tags'].description)
