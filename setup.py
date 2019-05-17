import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.read().split('\n')

setuptools.setup(
    name="PW_explorer",
    version="0.0.24",
    author="Sahil Gupta",
    author_email="",
    description="An Extensible Possible World Explorer for Answer Set Programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idaks/PW-explorer",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)