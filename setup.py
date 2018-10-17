from setuptools import setup

requires = [
    'luigi==2.7.9',
    'biopython==1.72'
]

setup(
    name='Extensions for Luigi based on Biopython',
    version='0.1',
    install_requires=requires,
    packages=['luigibio']
)

