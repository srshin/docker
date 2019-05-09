FROM node
ENV NODE_ENV=production
ADD . /src
WORKDIR /src

RUN nom install
CMD ["node", "app.js"]
