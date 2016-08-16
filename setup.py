import os

from setuptools import setup

requirements = [l.split('=')[0] for l in open('requirements.txt', 'r').read().split('\n') if l]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='tqcli',
    version='1.0',
    description=read('README.md'),
    url='http://github.com/tranquant/tqcli',
    author='Mehrdad Pazooki, Sean Glover, Rodrigo Abreu',
    author_email='mehrdad@tranquant.com',
    license='Apache 2.0',
    install_requires=requirements,
    entry_points={'console_scripts': ['tqcli=tqcli.tqcli:main']},
    package_dir={'tqcli': 'tqcli'},
    packages=['tqcli', 'tqcli.batch', 'tqcli.config'],
    keywords = ['dataset', 'data', 'apache spark', 'data science', 'big data', 'data marketplace', 'tranquant'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    zip_safe=True
)