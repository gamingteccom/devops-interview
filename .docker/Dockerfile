FROM php:apache

ENV APP_ENV=production

RUN apt update && apt upgrade -y
RUN apt install -y python3

RUN mkdir /build && mkdir /app
COPY . .
RUN python3 build.py
RUN cp public/index.php /app/
# fix permissions
RUN chmod 777 -R /app

ENV APACHE_DOCUMENT_ROOT /app

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# save space
RUN apt remove -y python3 && apt clean

EXPOSE 80
