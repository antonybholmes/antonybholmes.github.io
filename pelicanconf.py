#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Antony B Holmes'
SITENAME = 'Antony B Holmes'
SITEURL = '/antonyholmes'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITEURL = "."

LOAD_CONTENT_CACHE = False

STATIC_PATHS = ['images', 'css']
INDEX_SAVE_AS = 'articles/index.html'
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/index.html'
CATEGORY_URL = 'articles/category/{slug}/'
CATEGORY_SAVE_AS = 'articles/category/{slug}/index.html'
TAG_URL = 'articles/tag/{slug}/'
TAG_SAVE_AS = 'articles/tag/{slug}/index.html'
AUTHOR_URL = 'articles/author/{slug}/'
AUTHOR_SAVE_AS = 'articles/author/{slug}/index.html'
DRAFT_URL = 'articles/draft/{slug}/'
DRAFT_SAVE_AS = 'articles/draft/{slug}/index.html'


PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')

SITEMAP_SAVE_AS = 'sitemap.xml'

PAGE_EXCLUDES = ['templates']
ARTICLE_EXCLUDES = ['templates']


OUTPUT_PATH = '.'


#JINJA2CONTENT_TEMPLATES = ['content',]
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['jinja2content']
