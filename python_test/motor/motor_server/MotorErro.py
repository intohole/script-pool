#!/usr/bin/env python
# coding=utf-8

'''
Motor异常类
'''
class TokenUpdateErro(Exception):
    """Weibopy exception"""

    def __init__(self, reason):
        self.reason = reason.encode('utf-8')

    def __str__(self):
        return self.reason
