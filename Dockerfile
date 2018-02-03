FROM aqqwbjgyiy/centos7-with-pip 
MAINTAINER ouyangqiong

RUN yum install nginx uwsgi -y 
RUN yum install python-devel openssl-devel gcc-c++ -y
RUN yum install -y mysql-devel
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
ADD potato /opt/potato
COPY nginx-conf/potato.conf /etc/nginx/sites-available/default
RUN mkdir /var/log/potato
WORKDIR /scripts/
COPY nginx-conf/potato-uwsgi.ini /scripts/
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

