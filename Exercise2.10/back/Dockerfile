# start from node version 16 image
FROM golang:1.16

# expose container port
EXPOSE 8000

# working directory definition
WORKDIR /home/golang/app

# copy source
COPY . .

# build and give run rights to executable
RUN go build
RUN chmod u+x ./server

# start server
CMD ["./server"]
