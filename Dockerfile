FROM ubuntu:18.04
WORKDIR /sat
COPY . .
ENV TZ=Asia/Taipei
RUN mkdir var && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get update && \
    apt-get install -y python3-pip tzdata && \
    dpkg-reconfigure -f noninteractive tzdata && \
    pip3 install -r requirements.txt
EXPOSE 3000
CMD uwsgi -w main:app -s :3000 --logto var/sat.log