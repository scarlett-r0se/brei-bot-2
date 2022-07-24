#===============================================================================
#BRE-BOT 2.0 DOCKER FILE
#CREATED BY SCARLETT SMITH
#===============================================================================

#===============================================================================
#PULL LATEST DEBIAN DOCKER IMAGES
#===============================================================================
FROM debian:latest
#===============================================================================

#===============================================================================
#INSTALL APT PACKAGES
#===============================================================================
RUN apt update -y && \
    apt install \
    tmux \
    libasound2 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libsqlite3-dev \
    libreadline-dev \
    libffi-dev \
    curl \
    libbz2-dev \
    wget \
    iputils-ping \
    nano \
    -y
#===============================================================================


#===============================================================================
#DOWNLOAD AND INSTALL PYTHON 
#===============================================================================
WORKDIR /opt

RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz

#EXTRACT PYTHON 3.9 ARCHIVE
RUN tar -xvf Python-3.9.1.tgz

WORKDIR /opt/Python-3.9.1

#CONFIGURE PYTHON 3.9
RUN ./configure --enable-optimizations

#COMPILE PYTHON 3.9
RUN make -j 8

#INSTALL PYTHON 3.9
RUN make altinstall

#INSTALL PYTHON DEPENDENCIES

RUN pip3.9 install \
discord \
aiohttp==3.7.4 \
mcrcon \
python-dotenv
#===============================================================================


#===============================================================================
#INSTALL JAVA
#===============================================================================
WORKDIR /opt
#WGET JAVA
RUN wget https://download.bell-sw.com/java/17.0.4+8/bellsoft-jdk17.0.4+8-linux-amd64.deb
RUN dpkg -i bellsoft-jdk17.0.4+8-linux-amd64.deb

#===============================================================================
#SETUP DISCORD BOT
#===============================================================================
COPY ./discordBot /discordBot
ENTRYPOINT [ "python3.9" ]
CMD [ "/discordBot/bb2.py" ]
#===============================================================================






