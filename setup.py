from setuptools import setup, find_packages

setup(
    name='PyGit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "GitPython==3.1.40"
    ],
    entry_points={
        'console_scripts': [
            'pygit = src.main:main',
        ],
    },
)