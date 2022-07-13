from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    readme = fh.read()
with open('requirements.txt', 'r') as fh2:
    reqs = fh2.read()

setup(
    name='PyLoadBar',
    version="0.1.0",
    description=
    'Customizeable loading sequence/progress bar generator, enabling users to customize start/finish messages, toggle sequence type, and set total iterations among other features.',
    url='https://github.com/schlopp96/PyLoadBar',
    author='schlopp96',
    author_email='schloppdaddy@gmail.com',
    license='GPL v3.0',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[reqs],
    extras_require={"dev": ["pytest>=6.2.5"]},
    classifiers=[
        "Development Status :: 3 - Alpha", "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10", "Topic :: Utilities"
    ],
    keywords=[
        'python, load, bar, loading, sequence, progress, simple, easy, utilities, package, module, tqdm, pytest, pyloadbar, developer, tool, tqdm'
    ])
