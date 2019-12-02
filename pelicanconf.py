#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ales Stibal <astib@mag0.net>'
SITENAME = 'Smithproxy - (not only) tls mitm proxy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Smithproxy GIT', 'https://bitbucket.org/astibal/smithproxy/'),
         ('Socle library GIT', 'https://bitbucket.org/astibal/socle/'),
            ('pplay', 'https://pypi.org/project/pplay/'),
         )

# Social widget
SOCIAL = (('Smithproxy & tools discord', 'https://discord.gg/vf4Qwwt'),
          ('Mailing list', 'mailto:smithproxy-users@googlegroups.com'),
          ('Become a patron', 'https://www.patreon.com/bePatron?u=23520766'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
