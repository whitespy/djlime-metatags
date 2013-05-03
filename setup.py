from os.path import join, dirname
from setuptools import setup, find_packages


def long_description():
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return ''

setup(
    name='djlime-metatags',
    author='Andrey Butenko',
    author_email='whitespysoftware@yandex.ru',
    url='https://github.com/whitespy/djlime-metatags',
    description='''Django application for attaching meta-tags to objects and
     URL-path.''',
    long_description=long_description(),
    version='0.9.3',
    packages=find_packages(),
    include_package_data=True,
    platforms='any'
)
