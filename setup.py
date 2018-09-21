import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PW-explorer",
    version="0.0.1",
    author="Sahil Gupta",
    author_email="",
    description="An Extensible Possible World Explorer for Answer Set Programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idaks/PW-explorer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: Apache License, Version 2.0 (Apache-2.0)",
        "Operating System :: OS Independent",
    ],
    scripts=['PW-explorer/run_clingo.py', 'PW-explorer/load_worlds.py', 'PW-explorer/export.py',
             'PW-explorer/dist_calc.py', 'PW-explorer/complexity_calc.py', 'PW-explorer/pwe_query.py',
             'PW-explorer/visualize.py'
             ],
)