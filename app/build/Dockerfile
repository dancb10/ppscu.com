FROM python:3.7-alpine3.11

RUN echo https://sjc.edge.kernel.org/alpine/v3.11/main > /etc/apk/repositories \
    && echo https://sjc.edge.kernel.org/alpine/v3.11/community >> /etc/apk/repositories \
    && adduser app -Du 2342 -h /home/app \
    && ln -s /usr/local/bin/python /usr/bin/python \
    && apk add --virtual=build bash gcc libffi-dev musl-dev linux-headers openssl-dev make \
    && apk add --virtual=wget busybox-extras curl postgresql-dev
ENV HOME=/home/app
ADD src $HOME/
ADD build/db-migrate.sh $HOME/
RUN chmod 777 $HOME/db-migrate.sh
WORKDIR /home/app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]
