# The base image for the chatbot
FROM node:14

# Set the working directory
WORKDIR /app

# Copy all files and folders from current directory to container
COPY . /app
COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]