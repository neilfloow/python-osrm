# -*- coding: utf-8 -*-
"""
Python wrapper for osrm API v5
------------------------------
Wrap OSRM services 'route', 'nearest', 'table', 'match' and 'trip'.
Allow geometry decoding for 'viaroute', 'match' and 'trip' functions.
"""
__version__ = '0.11.1'


class DefaultRequestConfig:
    host = "http://localhost:5000"
    profile = "driving"
    version = "v1"

    def __str__(self):
        return("/".join([self.host, '*', self.version, self.profile]))

    def __repr__(self):
        return("/".join([self.host, '*', self.version, self.profile]))

    @staticmethod
    def __call__(addr=None):
        if not addr:
            return DefaultRequestConfig()
        else:
            tmp = addr.split('/')
            cla = DefaultRequestConfig()
            cla.host = tmp[0]
            i = len(tmp)
            cla.version = tmp[i-2]
            cla.profile = tmp[i-1]
            return cla

RequestConfig = DefaultRequestConfig()

from .core import match, simple_route, nearest, table, trip, _chain
from .extra import access_isocrone
