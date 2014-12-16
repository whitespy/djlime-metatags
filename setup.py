import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


setup(
    name='djlime-metatags',
    version='0.9.12',
    author='Andrey Butenko',
    author_email='whitespysoftware@yandex.ru',
    url='https://github.com/whitespy/djlime-metatags',
    description='''Django application for attaching meta-tags to objects and
     URL-path.''',
    long_description=README,
    packages=find_packages(),
    include_package_data=True,
    platforms='any'
)
