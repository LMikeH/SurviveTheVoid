from setuptools import setup, find_packages

setup(
    name="Survive The Void",
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'survivethevoid = survivethevoid.__main__:main'
        ]
    }
)
