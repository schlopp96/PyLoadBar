from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    readme = fh.read()

setup(
    name='PyLoadBar',
    version='0.0.7',
    description='Simple, easy-to-use loading sequence/progress bar module.',
    url='https://github.com/schlopp96/PyLoadBar',
    author='schlopp96',
    author_email='schloppdaddy@gmail.com',
    license='GPL v3.0',
    long_description=readme,
    long_description_content_type='text/plain',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['setuptools>=58.1.0', 'tqdm>=4.62.3'],
    extras_require={"dev": ["pytest>=6.2.5"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    keywords=
    'python load bar loading progress simple easy utilities useful package module tqdm pytest pyloadbar'
)
