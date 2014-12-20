# -*- encoding:utf-8 -*-
'''
'''
import re


class QiitaResponse():
    def __init__(self, response):
        self.response = response
        self.headers = response.headers
        self.table = {}

    @property
    def to_json(self):
        return self.response.json()

    @property
    def status(self):
        return self.response.status_code

    def _get_from_header(self, key):
        return self.headers[key] if key in self.headers else None

    @property
    def result_count(self):
        return self._get_from_header('Total-Count')

    @property
    def remain_request_count(self):
        return self._get_from_header('Rate-Remaining')

    @property
    def links(self):
        if self.table:
            return self.table
        links = self._get_from_header('Link').split(',')
        pattern = re.compile(r'<(.+?)>; rel="(.+?)"')
        for link in links:
            url, rel = pattern.findall(link.strip())[0]
            self.table[rel] = url
        return self.table

    @property
    def link_first(self):
        return self.links['first']

    @property
    def link_next(self):
        return self.links['next']

    @property
    def link_last(self):
        return self.links['last']
