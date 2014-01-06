#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'\u6cfd'
SITENAME = u'\u6cfd\u4ed4'
SITENAME = u'码农ing'
ARTICLE_URL = 'post/{date:%Y}-{date:%m}-{date:%d}-{slug}/'
ARTICLE_SAVE_AS = 'post/{date:%Y}-{date:%m}-{date:%d}-{slug}/index.html'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zhs'

SITESUBTITLE = u'迷茫在路上'
# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None




# Blogroll
LINKS = (('GitHub', 'https://github.com/intoblack/'),
         ('CSDN', 'http://www.csdn.net/'),)

# Social widget
SOCIAL = (('WeiBo', 'http://weibo.com/1152049780'),)

DEFAULT_PAGINATION = 6

THEME = "bootstrap2"
RANDOM = 'random.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
