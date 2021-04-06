import os
from setuptools import find_packages, setup


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
REQUIREMENTS_PATH = BASE_DIR + '/requirements.txt'
REQUIRED = []
if os.path.isfile(REQUIREMENTS_PATH):
    with open(REQUIREMENTS_PATH) as f:
        REQUIRED = f.read().splitlines()

setup(
    name='corellia_preprocessor',
    packages=find_packages(include=['corellia_preprocessor']),
    version='1.0.0',
    description='Corellia data market Preprocessor package',
    author='Boris Vasilev',
    author_email='borisvasilev395@gmail.com',
    license='MIT',
    install_requires=REQUIRED,
)
