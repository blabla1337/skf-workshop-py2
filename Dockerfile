FROM codercom/code-server:1.604-vsc1.32.0
MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>

RUN apt-get update && apt-get install -y python3 \
python3-dev \
python3-pip \ 
git

COPY --chown=root:root . /app
WORKDIR /app
RUN pip3 install -r target/requirements.txt
CMD [ "code-server", "/app/target", "--data-dir=/app/target", "--allow-http", "--password=workshop" ]


