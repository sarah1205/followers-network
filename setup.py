from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='followers',
    version='0.0.1',
    description='GitHub Follower Network Visualizer',
    long_description=readme,
    author='Arnaud Legendre',
    author_email='arnaudleg@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'followers = followers.main:main',
        ],
    },
)
