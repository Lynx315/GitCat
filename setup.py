from setuptools import setup

setup(
    name='gitcat',
    version='0.1',
    packages=['gitcat'],        # your package folder
    entry_points={
        'console_scripts': [
            'gitcat = gitcat.main:dispatcher',  # makes `gitcat` a CLI
        ],
    },
)
