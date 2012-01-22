#!/usr/bin/env python

from __future__ import print_function

import argparse
import datetime
import json
import logging
import multiprocessing
import os
import random
import time

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from logging.config import dictConfig
dictConfig(settings.LOGGING)

logger = logging.getLogger(__name__)

import requests

uwsgi_fmt = """
{root}/bin/uwsgi \
        --home {root} \
        --socket {host}:{port} \
        --module wsgi \
        --pythonpath {site_dir} \
        --master \
        --uid nobody \
        --gid nogroup \
        --no-orphans \
        --disable-logging \
        --processes {processes} \
        --max-requests {max_requests}
"""

class Command(BaseCommand):

    def handle(self, addrport='', *args, **options):

        host = getattr(settings, 'UWSGI_HOST', 'localhost')
        if host == '<AWS>':
            host = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').content

        debug = getattr(settings, 'DEBUG', False)
        if debug == False:
            max_requests = 0
        else:
            max_requests = 1

        uwsgi_cmd = uwsgi_fmt.format(
            root=settings.SITE_ROOT + '/..',
            site_dir=settings.SITE_ROOT,
            host=host,
            processes=multiprocessing.cpu_count(),
            port=settings.UWSGI_PORT,
            max_requests=max_requests)

        logger.info(uwsgi_cmd)
        os.system(uwsgi_cmd)
