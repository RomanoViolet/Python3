#
# Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu
# https://blobfolio.com/2018/12/using-docker-as-a-build-environment/

# Pull base image.
FROM ubuntu:20.04

# On single RUN command: https://coderwall.com/p/4g8znw/things-i-learned-while-writing-a-dockerfile
LABEL Python3Docker.version="0.1"
LABEL vendor="Devendra Rai, rai.devendra@yahoo.co.uk"
LABEL Python3Docker.release-date="2020-08-21"
LABEL Python3Docker.version.is-production="No"

ARG GTESTCOMMITID=cad3bc46c2ba8ec0bd7bb252d7279fe791140fbf
ARG USERNAME=dockeruser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Tell debian that we are running non-interactively
ENV DEBIAN_FRONTEND=noninteractive

# Install Core components.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -qqy upgrade && \
  apt-get -y install --no-install-recommends apt-utils dialog 2>&1 && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y sudo && \
  apt-get install -qqy libz-dev && \
  apt-get install -qqy gnupg && \
  apt-get install -qqy curl && \
  apt-get install -qqy net-tools && \
  apt-get install -qqy wget && \
  apt-get install -qqy bash && \
  apt-get install -qqy xz-utils && \
  apt-get install -qqy python3 pylint python3-pandas python3-matplotlib ipython3 python3-dev jupyter && \
  apt-get install -qqy apt-transport-https && \
  apt-get install -qqy python3 python3-pip && \
  apt-get install -qqy python3-jinja2 && \
  apt-get install -qqy make && \
  apt-get install -qqy git && \
  apt-get install -qqy locales && \
  #
  # Install PEP8 for Python formatting.
  pip3 install --upgrade autopep8 pylint && \
  #
  # Install Scrapy
  #
  pip3 install --upgrade scrapy && \
  apt-get purge -y --auto-remove build-essential && \
  apt-get purge -y --auto-remove software-properties-common && \
  apt-get purge -y --auto-remove curl wget && \
  apt-get purge -y --auto-remove xz-utils && \
  #apt-get purge -y --auto-remove python3-pip && \
  apt-get purge -y --auto-remove apt-transport-https && \
  apt-get autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  #update-alternatives --install /usr/bin/clang clang /usr/bin/clang-8 100 && \
  #
  # Setup locales
  sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=en_US.UTF-8 && \
  #
  # Add non-admin user
  #
  groupadd --gid $USER_GID $USERNAME && \
  useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME && \
  echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
  chmod 0440 /etc/sudoers.d/$USERNAME && \
  #
  # Make sure that all file in /home/dockeruser are owned by dockeruser
  #
  chown -R dockeruser /home/dockeruser
#ENV HOME /home/dockeruser && \
#

# Add default home for the non-admin user
WORKDIR /home/dockeruser
ADD --chown=dockeruser Configurations/.gitconfig /home/dockeruser/.gitconfig
ENV LANG en_US.UTF-8
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Do the following as an ordinary user
USER dockeruser

RUN \
  chmod +x /home/dockeruser/.bashrc
