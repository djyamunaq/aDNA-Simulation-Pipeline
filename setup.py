from setuptools import setup
setup(
    name = 'simulation-pipeline',
    version = '0.1.0',
    packages = ['src'],
    entry_points = {
        'console_scripts': [
            'simpipe = src.__main__:main'
        ]
    })