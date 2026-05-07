FROM node:20-alpine
WORKDIR /app
COPY . .
RUN npm init -y && npm install redis
EXPOSE 3000
CMD ["node", "app.js"]
