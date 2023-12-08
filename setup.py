from setuptools import setup
setup(
    name = 'simulation-pipeline',
    version = '0.1.0',
    packages = ['extension'],
    entry_points = {
        'console_scripts': [
            'sim = extension.__main__:main'
        ]
    })