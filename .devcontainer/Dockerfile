# See here for image contents:
FROM mcr.microsoft.com/azure-functions/python:4-python3.10-core-tools

WORKDIR /workspaces/app
ARG WORKSPACE_FOLDER="/workspaces/app"

# Install program dependencies:

RUN mkdir /tmp/config_container

#COPY /.devcontainer/install-deps.sh /tmp/config_container/install-deps.sh
#RUN chmod +x /tmp/config_container/install-deps.sh
#RUN /tmp/config_container/install-deps.sh

RUN rm -rvf /tmp/config_container

# Create virtual environment:

VOLUME $WORKSPACE_FOLDER/.venv
