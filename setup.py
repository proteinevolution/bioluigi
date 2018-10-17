from setuptools import setup

requires = [
    'luigi==2.7.9',
    'biopython==1.72'
]

setup(
    author='Lukas Zimmermann',
    author_email='luk.zim91@gmail.com',
    name='luigibio',
    description='Extensions for Spotify\'s luigi based on BioPython',
    version='0.1',
    install_requires=requires,
    packages=['luigibio']
)

