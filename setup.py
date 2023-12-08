from setuptools import setup
setup(
    name = 'simulation-pipeline',
    version = '0.1.0',
    packages = ['sim'],
    entry_points = {
        'console_scripts': [
            'sim = sim.__main__:main'
        ]
    })