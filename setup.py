from setuptools import setup

setup(
    name="Survive The Void",
    version='0.1',
    packages=['survivethevoid',
              'survivethevoid.assets',
              'survivethevoid.characters',
              'survivethevoid.environment'],
    entry_points={
        'console_scripts': [
            'survivethevoid = survivethevoid.__main__:main'
        ]
    }
)