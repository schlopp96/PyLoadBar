from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='PyLoadBar',
    version='0.0.5.1',
    description='Simple, easy-to-use loading sequence/progress bar module.',
    url='https://github.com/schlopp96/PyLoadBar',
    author='schlopp96',
    author_email='schloppdaddy@gmail.com',
    long_description=long_description,
    long_description_content_type='text/plain',
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['quickload=PyLoadBar.loadbar:main']},
    install_requires=['setuptools>=58.1.0', 'tqdm>=4.62.3'],
    extras_require={"dev": ["pytest>=6.2.5"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords=
    'python loading progress bar simple easy utilities useful package module')
