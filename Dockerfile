FROM jupyter/minimal-notebook:a238993ad594

USER root

# download dlv
RUN cd /opt && \
	wget http://www.dlvsystem.com/files/dlv.x86-64-linux-elf-static.bin -O dlv && \
	chmod +x dlv && \
	ln -s /opt/dlv /usr/bin


USER jovyan

# get the clingo binary file for linux
# and install 
# get the clingo binary file using conda install
RUN conda install -c potassco clingo=5.3.0 
RUN conda install -c anaconda graphviz=2.40.1
RUN conda install -c anaconda pygraphviz=1.3

# install PW_explorer	
RUN pip install PW_explorer

# go back to an earlier version of antlr4 (latest version might not work):
RUN pip install antlr4-python3-runtime==4.7.1

# prepare a home directory for answer set programming
RUN cd ~ && \
	mkdir asp


MAINTAINER Nikolaus Parulian <nikolaus.nova@gmail.com>
