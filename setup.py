from setuptools import setup, find_packages

setup(
    name = "django_image_sourceset",
    version = "0.1.0",
    description = 'Create a sourceset for an django image',
    author = 'Martin Gutmair',
    author_email = 'martin@gutmair.de',
    url = 'https://github.com/gudi1989/django_image_sourceset',
    long_description = open('README.rst', 'r').read(),
    packages = [
        'django_image_sourceset',
        'django_image_sourceset.management',
        'django_image_sourceset.management.commands',
        'django_image_sourceset.templatetags',
    ],
    install_requires = [
        'Django >=2.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

