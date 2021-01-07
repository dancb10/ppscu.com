FROM python:3.7-alpine3.11

RUN echo https://sjc.edge.kernel.org/alpine/v3.11/main > /etc/apk/repositories \
    && echo https://sjc.edge.kernel.org/alpine/v3.11/community >> /etc/apk/repositories \
    && adduser backend -Du 2342 -h /home/backend \
    && ln -s /usr/local/bin/python /usr/bin/python \
    && apk add --virtual=wget busybox-extras curl
USER backend
ENV HOME=/home/backend
ADD test $HOME/
WORKDIR /home/backend
EXPOSE 9090
CMD python backend_test.py
