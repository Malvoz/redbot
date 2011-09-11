#!/usr/bin/env python

from distutils.core import setup

setup(name='redbot',
      version='1.0',
      description='Resource Expert Droid',
      author='Mark Nottingham',
      author_email='mnot@mnot.net',
      url='http://redbot.org/project/',
      packages=['redbot', 
                'redbot.formatter', 
                'redbot.subrequest'
                'redbot.headers'],
      package_dir={'redbot': 'redbot'},
      scripts=['bin/redbot'],
      install_requires = ['thor >= 0.1'],
      classifiers=[
        'Programming Language :: Python'
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',      
      ],
)
