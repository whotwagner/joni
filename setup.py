from setuptools import setup

setup(name='joni',
      version='0.1',
      description='Joni plays music for children',
      url='http://github.com/whotwagner/joni',
      author='Wolfgang Hotwagner',
      author_email='code@feedyourhead.at',
      license='GPL',
      packages=['joni'],
      install_requires=[
      'pyyaml',
      'pydantic',
      'python-mpd2'
      ],
      zip_safe=False)
