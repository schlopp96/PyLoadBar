from os import name
from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='PyLoadBar',
      version='0.0.2',
      description='Simple, easy-to-use loading sequence/progress bar module.',
      py_modules=["PyLoadBar"],
      package_dir={'': 'src'},
      classifiers=[
          "Development Status :: 1 - Planning",
          "Programming Language :: Python :: 3.0",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
      long_description=long_description,
      long_description_content_type='text/plain',
      install_requires=['setuptools>=58.1.0', 'tqdm==4.62.3'],
      extras_require={"dev": ["pytest>=6.2.5"]},
      url='https://github.com/schlopp96/PyLoadBar',
      author='Schlopp96',
      author_email='schlopp96@gmail.com')
