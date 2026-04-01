FROM node

ENV APP_ENV=production

RUN apt update && apt upgrade -y
RUN apt install -y python3

RUN mkdir /build && mkdir /app
COPY . .
RUN python3 build.py
RUN cp public/index.js /app/
# fix permissions
RUN chmod 777 -R /app

# save space
RUN apt remove -y python3 && apt clean

EXPOSE 3000

CMD ["node", "/app/index.js"]
