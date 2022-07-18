from setuptools import setup, find_packages

# For consistent encoding
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="kuda-python",
    version="1.0.0",
    description="Kuda OpenAPI Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://kuda-python.readthedocs.io/",
    author="Chiemezie Njoku",
    author_email="njokuchiemezie01@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["kuda"],
    include_package_data=True,
    install_requires=["requests"]
)