# -*- encoding:utf-8 -*-
'''
'''
import requests
import yaml
from exception import QiitaApiException

class QiitaClientBase():
    ''' Python Client Base for Qiita API v2
    '''
    HOST = 'qiita.com'
    USER_AGENT = 'Qiita python3 binding'
    ACCEPT = 'application/json'
    HEADER = {
        'Accept': ACCEPT,
        'User-Agent': USER_AGENT,
    }

    def __init__(self, config_file=None, access_token=None, debug=False):
        ''' initialize instance with ACCESS_TOKEN
        :param config_file: yaml file includes ACCESS_TOKEN: <your_token>
        :param access_token: <your_token>
        :param debug: _request returns requests.Response instance if True
        '''
        if config_file:
            with open(config_file, 'r') as f:
                config = yaml.load(f)
                self.access_token = config['ACCESS_TOKEN']
        else:
            self.access_token = access_token
        self.debug = debug

    def _url_prefix(self):
        ''' url prefix for api endpoint
        >>> client._url_prefix()
        'https://qiita.com/api/v2'
        '''
        return 'https://{}/api/v2'.format(self.HOST)

    def header(self):
        ''' make request header
        >>> header = client.header()
        >>> minimal_header = set(['Authorization', 'Accept', 'User-Agent'])
        >>> set(header.keys()).issuperset(minimal_header)
        True
        '''
        if self.access_token:
            self.HEADER.update(
                {'Authorization': ' Bearer {}'.format(self.access_token)})
        return self.HEADER

    def _request(self, method, url, params=None, headers=None):
        ''' alias for request with requests module
        Returns requests.models.Response instance

        :param method: "GET", "POST", "PUT", "DELETE", "PATCH"
        :param url: request url
        :param params: dictionary to be sent
        :param headers: dictionary of Http Headers to be sent
        '''
        headers = self.header() if headers is None else headers
        if type(headers) is not dict:
            return TypeError('headers must be dictionary')

        method = method.upper()
        if method in ('GET', 'DELETE'):
            response = requests.request(
                method=method, url=url, headers=headers, params=params)
        elif method in ('POST', 'PUT', 'PATCH'):
            response = requests.request(
                method=method, url=url, headers=headers, json=params)
        else:
            raise Exception('Unknown method')

        if response.ok:
            if self.debug:
                return response
            return response.json()
        else:
            if self.debug:
                return response
            raise QiitaApiException(response.json())

    def request(self, method, path, params=None, headers=None):
        ''' alias for request with self._request method
        Returns requests.models.Response instance

        :param method: "GET", "POST", "PUT", "DELETE", "PATCH"
        :param path: request path for qiita api (e.g. /users/petitviolet)
        :param params: dictionary to be sent
        :param headers: dictionary of Http Headers to be sent
        '''
        url = self._url_prefix() + path
        return self._request(method, url, params, headers)

    def get(self, path, params=None, headers=None):
        ''' get request
        >>> client.get('/users/petitviolet').status_code
        200
        '''
        return self.request('GET', path, params, headers)

    def post(self, path, params=None, headers=None):
        ''' post request
        >>> from datetime import datetime
        >>> now = datetime.today()
        >>> res = client.post('/items', \
                        params={ \
                            'body': 'python api client test:', \
                            'coediting': False, \
                            'gist': False, \
                            'private': False, \
                            'tags': [{'name': 'python', 'versions': ['3.4.1']}], \
                            'title': 'test for python client {}'.format(now), \
                            'tweet': False, \
                        })
        >>> res.status_code
        201
        >>> res = client.delete('/items/{}'.format(res.json()['id']))
        >>> res.status_code
        204
        '''
        return self.request('POST', path, params, headers)

    def put(self, path, params=None, headers=None):
        ''' put request
        '''
        return self.request('PUT', path, params, headers)

    def patch(self, path, params=None, headers=None):
        ''' patch request
        '''
        return self.request('PATCH', path, params, headers)

    def delete(self, path, params=None, headers=None):
        ''' delete request
        '''
        return self.request('DELETE', path, params, headers)

def test():
    import doctest
    doctest.testmod(extraglobs={'client': QiitaClient('../config.yml')})

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()
    else:
        print('Enjoy Qiita!!!')
