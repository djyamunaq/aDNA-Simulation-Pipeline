from setuptools import setup
setup(
    name = 'simulation-pipeline',
    version = '0.1.0',
    packages = ['simpipe'],
    entry_points = {
        'console_scripts': [
            'simpipe = simpipe.__main__:main'
        ]
    })