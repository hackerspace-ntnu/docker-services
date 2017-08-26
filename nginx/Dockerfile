FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

RUN apt-get update && apt-get install -y \
    nano \
    net-tools \
    curl \
    iputils-ping

COPY sites-enabled/* /etc/nginx/conf.d/

# Create folder for certs, and copy certs from server into container
RUN mkdir certs
COPY /etc/ssl/certs/dhparam.pem /certs/dhparam.pem
