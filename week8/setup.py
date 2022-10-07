from setuptools import setup, find_packages


setup(
    name='movierental',
    version='0.2',
    author='Paola Cartala',
    author_email='pcartala@applaudiostudios.dev',
    packages=find_packages(exclude=["src/tests/"]),
)
