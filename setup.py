from setuptools import setup, find_packages

setup(
    name='text2audio_by_bark',
    version='0.1',
    author='author',
    author_email='author@email.com',
    description='convert text to audio by bark',
    packages=find_packages(),
    install_requires=[
        # List of required packages
        'bark',
    ],
)