from setuptools import setup, find_packages

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
                      'scipy',
                      'pygame >= 1.9.1',
                      'pyyaml'
                      ]
)
