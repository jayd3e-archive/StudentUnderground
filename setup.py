#StudentUnderground/setup.py
from setuptools import setup

setup(name='StudentUnderground',
      version='0.1dev',
      description='A social homework collaboration site for students.',
      long_description='',
      install_requires=['pyramid',
                        'mako',
                        'sqlalchemy',
                        'pyramid_handlers',
                        'pyramid_tm',
                        'MySQL-python',
                        'weberror',
                        'nose',
                        'coverage',
                        'colander',
                        'deform'],
      url='http://localhost',
      packages=['studentunderground'],
      test_suite='studentunderground',
      entry_points = """\
      [paste.app_factory]
      main = studentunderground:main
      """,
      )
