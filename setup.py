from setuptools import setup, find_packages

setup(
    name='text2audio_by_bark',
    version='0.1',
    author='author',
    author_email='author@email.com',
    description='convert text to audio by bark',
    entry_points={"console_scripts": ["text2audio_by_bark=text2audio_by_bark.text2audio:test_main"]},
    packages=find_packages(),
    install_requires=[
        # List of required packages
        'bark',
    ],
    #py_modules=['funcs'],
    #package_dir={'': 'src'},
)
