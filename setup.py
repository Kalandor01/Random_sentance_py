from setuptools import setup, find_packages

from random_sentance import __version__

setup(
    name='random_sentance',
    version=__version__,

    url='https://github.com/Kalandor01/random_sentance',
    author='Kalandor01',
    author_email='rohovszkyakoska@gmail.com',

    packages=find_packages(),

    install_requires=[
        'simpleaudio',
    ],
)
