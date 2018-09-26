import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.read().split('\n')

setuptools.setup(
    name="PW_explorer",
    version="0.0.2",
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
    scripts=['PW_explorer/run_clingo.py', 'PW_explorer/load_worlds.py', 'PW_explorer/export.py',
             'PW_explorer/dist_calc.py', 'PW_explorer/complexity_calc.py', 'PW_explorer/pwe_query.py',
             'PW_explorer/visualize.py', 'PW_explorer/pwe_helper.py'
             ],
)