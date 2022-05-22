# start from node version 16 image
FROM node:16

# expose container port
EXPOSE 5000

# working directory definition
WORKDIR /home/node/app

# dependencies are defined in these files, install before source build (layering)
COPY package* ./

# install dependencies defined in package.json
RUN npm install

# install serve
RUN npm install -g serve

# copy source files to container,
# build in production mode
COPY . .
RUN npm run build

# start serve
CMD ["serve", "-s", "-l", "5000", "build"]