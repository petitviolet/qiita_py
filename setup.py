''' Wrapper for Qiita API v2

created by @petitviolet
http://petitviolet.mit-license.org/
'''

import os
from setuptools import setup, find_packages
from qiita_v2 import (__author__, __license__, __version__, __name__)

long_desc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name=__name__,
    author=__author__,
    version=__version__,
    license=__license__,
    author_email='violethero0820@gmail.com',
    url='http://github.com/petitviolet/qiita_py',
    description='Python Wrapper for Qiita API v2',
    long_description=long_desc,
    platforms='any',
    packages=find_packages(),
    install_requires=['pyyaml', 'requests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
