FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.11

ENV DEBIAN_FRONTEND=noninteractive
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    curl \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=dialog