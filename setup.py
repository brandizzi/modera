#!/usr/bin/env python
from setuptools import setup

setup(name = 'modera',
      version = '0.1.0',
      #download_url = 'https://bitbucket.org/brandizzi/modera/???',
      description = "Modera - an application for managing the moderation/revision of things",
      author = "Adam Victor Nazareth Brandizzi",
      author_email = 'brandizzi@gmail.com',
      packages = ['modera'],
      maintainer = 'Adam Victor Nazareth Brandizzi ',
      maintainer_email = 'brandizzi@gmail.com',
      url = 'http://bitbucket.org/brandizzi/modera/',
      long_description = """\
Modera is an application for managing the moderation/revision of things - for now, specially, videos

It is web based, written in CherryPy, Cheetah e SQLAlchemy.
      """,
      classifiers = ['Development Status :: 1 - Planning',
                     'Environment :: Web Environment',
                     'Framework :: CherryPy',
                     'Intended Audience :: Information Technology',
                     'Intended Audience :: Education',
                     'Intended Audience :: Publishing Industry',
                     'Intended Audience :: System Administrators',
                     'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                     'Natural Language :: English',
                     'Natural Language :: Portuguese',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Programming Language :: Retwill',
                     'Topic :: Education',
                     'Topic :: Office/Business',
                     ],

      test_suite = 'unittest2',
      install_requires = ['cherrypy', 'cheetah', 'sqlalchemy'],
      tests_require =  ['unittest2', 'retwill'],
      )
