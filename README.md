# An Extensible Possible Worlds Explorer for Answer Set Programming

### To get started (using Conda) -- recommended

1. ```conda create -n your-pwe-env-name```
2. Install DLV from [here](http://www.dlvsystem.com/dlv/#1) and ensure it is available in the path.
3. ```conda install -c potassco clingo ```
4. ```conda install -c anaconda graphviz```
5. ```conda install -c anaconda pygraphviz```
6. ```pip install PW_explorer```

(To use PWE in Jupyter Notebooks, install Jupyter)

7. ```conda install -c anaconda jupyter```

### To Get Started (using venv):

1. Install clingo. PW_explorer has been tested with clingo version: 5.2.1

2. Install DLV.

3. Make sure the packages graphviz>=0.8.2 and pygraphviz>=1.5 are installed. These are required to be able to use the visualization functionality. You can find instructions to install pygraphviz [here](http://pygraphviz.github.io/documentation/pygraphviz-1.3.1/install.html).

These commands usually work as well:

  a.  ```apt-get install python-dev graphviz libgraphviz-dev pkg-config``` OR ```brew install graphviz``` 

  b.  ```pip3 install pygraphviz```
  
  (Might need to run them using sudo)
  
  [StackOverflow Reference](https://stackoverflow.com/questions/40528048/pip-install-pygraphviz-no-package-libcgraph-found)

4. ```python3 -m venv /path/to/new/virtual/environment```

5. ```source /path/to/new/virtual/environment/bin/activate```

6. ```python3 -m pip install PW_explorer```

To deactivate the virtualenv after you're done working:

7. ```deactivate```

Repeat Step 5 to resume work and Step 7 to exit the virtualenv again.


#### Launch a ASP+PWE friendly computing environment on Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/idaks/PW-explorer/master)

### General System Architecture:

![PWE-UML-Diagram](https://user-images.githubusercontent.com/14302941/54492765-54b63680-4897-11e9-933b-3efc34eb7106.png)


#### PWE Demos available [here](https://github.com/idaks/PWE-demos)
