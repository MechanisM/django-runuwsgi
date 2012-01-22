django-runuwsgi
==========================
**Integrate running uwsgi and manage.py.**

This app integrates virtualenv, uwsgi and manage.py along with some support 
for ec2. It meant for use in conjuction with upstart. If ``UWSGI_HOST`` is to
``<AWS>`` the host passed to --socket is set to the instance's private ip
address.

.. contents:: Contents
    :depth: 5

Installation
------------
#. Get the source.::

    pip install -e git+https://github.com/dpetzold/django-runuwsgi

#. Update INSTALLED_APPS your project's ``settings.py``::

    'runuwsgi',

#. Update ``settings.py``.::

    UWSGI_HOST = 'localhost'
    UWSGI_PORT = 9000

#. Try running the server. ::

    python manage.py runserver_uwsgi

#. Add the upstart config to ``/etc/init/{site_name}.conf``.::

    # file: /etc/init/{site_name}.conf
    description "uWSGI server for example.com"

    start on runlevel [2345]
    stop on runlevel [!2345]

    respawn

    exec {site_dir}../bin/python {site_dir}/manage.py runserver_uwsgi >> /var/log/uwsgi.log 2>&1

#. Verify upstart works.::

    start {site_name}
    restop {site_name}
    stop {site_name}
