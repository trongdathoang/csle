FROM debian:10.2

RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    debconf-utils && \
    echo mariadb-server mysql-server/root_password password vulnerables | debconf-set-selections && \
    echo mariadb-server mysql-server/root_password_again password vulnerables | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    apache2 \
    mariadb-server \
    php \
    php-mysql \
    php-pgsql \
    php-pear \
    php-gd \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY docker_files/web_dvwa_base/docker/php.ini /etc/php5/apache2/php.ini
COPY docker_files/web_dvwa_base/docker/php.ini /etc/php/7.3/apache2/php.ini
COPY docker_files/web_dvwa_base/docker/dvwa /var/www/html

COPY docker_files/web_dvwa_base/docker/config.inc.php /var/www/html/config/

RUN chown www-data:www-data -R /var/www/html && \
    rm /var/www/html/index.html

RUN service mysql start && \
    sleep 3 && \
    mysql -u root -pvulnerables -e "CREATE USER app@localhost IDENTIFIED BY 'vulnerables';CREATE DATABASE dvwa;GRANT ALL privileges ON dvwa.* TO 'app'@localhost;"


COPY docker_files/web_dvwa_base/docker/main.sh /
RUN chmod 777 /main.sh
#ENTRYPOINT ["/main.sh"]