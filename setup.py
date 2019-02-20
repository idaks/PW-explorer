import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.read().split('\n')

setuptools.setup(
    name="PW_explorer",
    version="0.0.13",
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
    scripts=['PW_explorer/PWE_CLI_Scripts/pwe_run_clingo', 'PW_explorer/PWE_CLI_Scripts/pwe_load_worlds',
             'PW_explorer/PWE_CLI_Scripts/pwe_complexity_calc', 'PW_explorer/PWE_CLI_Scripts/pwe_dist_calc',
             'PW_explorer/PWE_CLI_Scripts/pwe_export', 'PW_explorer/PWE_CLI_Scripts/pwe_query',
             'PW_explorer/PWE_CLI_Scripts/pwe_visualize', 'PW_explorer/PWE_CLI_Scripts/pwe_run_dlv'
             ]
)