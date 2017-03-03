from distutils.core import setup
import os

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(
  name='germantournament',
  packages=['germantournament'],  # this must be the same as the name above
  version='0.1.1',
  description='A package for help schedule tournaments',
  long_description=long_description,
  author='Orcun Gumus',
  author_email='orcungumus@gmail.com',
  url='https://github.com/guemues/german-game-tournament',  # use the URL to the github repo
  download_url='https://github.com/guemues/german-game-tournament/archive/0.1.1.tar.gz',  # I'll explain this in a second
  keywords=['tournament', 'german', 'game'],  # arbitrary keywords
  classifiers=[],
)