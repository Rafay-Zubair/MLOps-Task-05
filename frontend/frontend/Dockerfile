FROM node:20.8.0-alpine3.18

RUN mkdir app

WORKDIR /app

COPY package*.json ./

RUN npm install

EXPOSE 5173

ENV BACKEND_SERVICE_URL="backend-cont:9090"

COPY ./ ./

CMD ["npm", "run", "dev"]

