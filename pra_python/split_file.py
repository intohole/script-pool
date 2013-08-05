#!/usr/bin/env python
#
#
#
#
#
#
#

import re


reg = re.compile('[0-9]*\,')
print reg.match('23433,sdfasdf').group()
print reg.match('asdfasdf,ss')

