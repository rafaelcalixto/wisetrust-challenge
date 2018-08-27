####### Python 3.6
####### author: Rafael Calixto
####### created at: 08/26/2018
####### description: This file is a documentation and provide util
####### informations about the project.

from setuptools import setup

setup(
      name = 'wisetrust_challenge'
      version = '1.0'
      description = '''This is a challenge as part of the selective process
                       to the Data Engineer position at Wise Trust'''
      url = 'https://github.com/rafaelcalixto/'
      author = 'Rafael Calixto'
      license = 'MIT'
      packages = ['GUI', 'text_minning', 'scraper']
      install_requires = [
          'lxml',
          'jupyter',
          'bottle',
          'matplotlib',
          'nltk'
      ]
)
