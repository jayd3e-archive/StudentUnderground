#StudentUnderground/setup.py
from setuptools import setup

setup(name='StudentUnderground',
      version='0.1dev',
      description='A web-based note takeing application',
      long_description='',
      install_requires=['pyramid',
                        'mako',
                        'sqlalchemy',
                        'zope.sqlalchemy',
                        'repoze.tm2'],
      url='http://localhost',
      packages=['studentunderground'],
      test_suite='studentunderground',
      entry_points = """\
      [paste.app_factory]
      main = studentunderground:main
      """,
      )
