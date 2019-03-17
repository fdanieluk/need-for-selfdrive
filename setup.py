"""pip install -e .
"""


from setuptools import setup


setup(name='mynfs',
      version='0.0.1',
      description='Need for Speed selfdrive project',
      url='https://github.com/imintogoodmusic/need-for-selfdrive',
      author='Filip Danieluk',
      author_email='filip.danieluk94@gmail.com',
      license='MIT',
      packages=['nfs.src', 'nfs'],
zip_safe=False)