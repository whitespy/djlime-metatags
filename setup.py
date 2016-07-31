import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


setup(
    name='djlime-metatags',
    version='0.9.14',
    description='''
    Django application, that allows attach title, keywords and description meta tags for site's pages.
    ''',
    author='Andrey Butenko',
    author_email='whitespysoftware@yandex.ru',
    url='https://github.com/whitespy/djlime-metatags',
    long_description=README,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['django>=1.7']
)
