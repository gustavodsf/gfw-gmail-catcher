FROM python:3

LABEL Description="Image for Global Forest Watcher email downloader"

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/Detroit /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata


ENV TZ="America/Detroit"

WORKDIR /srv/src

COPY requirements.txt ./

RUN pip install --upgrade pip --user
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
