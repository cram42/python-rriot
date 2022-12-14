FROM mcr.microsoft.com/devcontainers/python:3.9-bullseye

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN pipx uninstall black
RUN pipx uninstall flake8
RUN pipx uninstall pydocstyle
RUN pipx uninstall pycodestyle
RUN pipx uninstall mypy
RUN pipx uninstall pylint

COPY requirements_dev.txt ./
RUN python3 -m pip install -r requirements_dev.txt
RUN rm -rf requirements_dev.txt

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt
RUN rm -rf requirements.txt

ENV SHELL /bin/bash
