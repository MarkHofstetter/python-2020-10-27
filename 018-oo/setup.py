from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Demo for OO and repo structure',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='bla@bli.at',
    url='https://github.com/MarkHofstetter',
    packages=find_packages(exclude=('tests', 'docs'))
)