FROM node:14.9
 
WORKDIR /frotend
 
COPY package*.json ./
 
RUN npm install
 
COPY . .
 
EXPOSE 3000
 
CMD [ "npx", "create-react-app myapp" ]

