from setuptools import setup, find_packages
# from cx_Freeze import setup, Executable
import sys

setup(
    name="Survive The Void",
    version='0.1',
    python_requires='>=3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'survivethevoid = survivethevoid.__main__:main'
        ]
    },
    install_requires=['numpy',
                      'pygame',
                      'pyyaml'
                      ],

)
