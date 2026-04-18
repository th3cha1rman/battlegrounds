####################################
#
#  Dev Container for Root the Box
#  Based on production Python 3.13 setup

FROM python:3.13-slim-bookworm

# Install system dependencies (matching production + dev tools)
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    zlib1g-dev \
    rustc \
    python3-pycurl \
    sqlite3 \
    libsqlite3-dev \
    default-libmysqlclient-dev \
    # Dev tools
    curl \
    git \
    vim \
    locales \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Generate locale for MySQL shell
RUN sed -Ei 's/^# en_US\.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen

# Copy and install Python dependencies
COPY ./setup/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --upgrade && \
    pip install --upgrade pylint debugpy

# Create dev user (matches your host UID for file permissions)
ARG USERNAME=rtbdev
ARG UID=1000
ARG GID=1000
RUN groupadd --gid $GID $USERNAME && \
    useradd --create-home --shell /bin/bash --uid $UID --gid $GID $USERNAME

# Create and set permissions for the application directory
RUN mkdir -p /home/rtbdev/code/files && \
    chown -R $USERNAME:$USERNAME /home/rtbdev/code

# Switch to dev user
USER $USERNAME

# Set working directory
WORKDIR /home/rtbdev/code

# Default command (can be overridden)
CMD ["python3", "rootthebox.py", "--setup=dev", "--start", "--debug"]