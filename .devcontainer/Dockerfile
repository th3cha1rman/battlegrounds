FROM python:3.8

# Install system dependencies including MySQL client
RUN apt-get -qq update \
	&& export DEBIAN_FRONTEND=noninteractive \
	&& apt-get -qq upgrade -y \
	&& apt-get -qq install -y --no-install-recommends \
		lsb-release \
		locales \
		build-essential \
		zlib1g-dev \
		python3-pycurl \
		default-mysql-client \
		wget \
		gnupg \
	&& apt-get autoremove -y \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/*

# Generate the en_US.UTF-8 locale
RUN sed -Ei 's/^# en_US\.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen

# Install Python dependencies
COPY ../setup/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --upgrade && pip install --upgrade pylint

# Create a new user dev (1000 matches the default user in macOS)
ARG USERNAME=rtbdev
ARG UID=1000
ARG GID=1000
RUN groupadd --gid $GID $USERNAME
RUN useradd --create-home --shell /bin/bash --uid $UID --gid $GID $USERNAME

# Run with dev user
USER $USERNAME
