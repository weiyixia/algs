import setuptools
from setuptools import setup, find_packages
setup(
    name='algs',
    version='0.1',
    packages=setuptools.find_packages('.') + setuptools.find_packages('src/.'),
    package_dir={'': 'src', 'test':'.'}
)
