####################################
#
#  Dockerfile for Root the Box
#  v0.1.4 - By Moloch, ElJeffe, Th3cha1rman
#
####################################

FROM python:3.13-slim-bookworm

RUN apt update && apt install -y --no-install-recommends \
build-essential pkg-config zlib1g-dev rustc \
python3-pycurl sqlite3 libsqlite3-dev default-libmysqlclient-dev

ADD ./setup/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --upgrade

ENV SQL_DIALECT=sqlite

RUN mkdir /opt/rtb
ADD . /opt/rtb

VOLUME ["/opt/rtb/files"]
ENTRYPOINT ["python3", "/opt/rtb/rootthebox.py", "--setup=docker"]