from sys import version_info
from setuptools import setup, find_packages

kwargs = {
    'name': 'django-runuwsgi',
    'version': '0.1',
    'description': 'Integrates uwsgi and manage.py.',
    'author': 'Derrick Petzold',
    'author_email': 'dpetzold@gmail.com',
    'url': 'http://github.com/dpetzold/django-runuwsgi/',
    'keywords': 'uwsgi,upstart,django',
    'license': 'BSD',
    'packages': [
        'runuwsgi',
    ],
    'include_package_data': True,
    'zip_safe': False,
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
}
setup(**kwargs)
