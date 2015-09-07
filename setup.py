import os
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'firebase-token-generator',
]

setup(
    name='suit-flame',
    version='0.1',
    packages=['suit_flame', 'suit_flame.templatetags'],
    include_package_data=True,
    license='BSD License',  # example license
    description='See active users & autosave changes at django admin.',
    author='hipo',
    url='https://github.com/hipo/django-suit-flame',
    author_email='pypi@hipolabs.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires
)
