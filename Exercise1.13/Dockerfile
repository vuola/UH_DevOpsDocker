# start from node version 16 image
FROM golang:1.16

# expose container port
EXPOSE 8080

# working directory definition
WORKDIR /home/golang/app

# copy source
COPY . .

# build and give run rights to executable
RUN go build
RUN chmod u+x ./server

# define environmental variables
ENV PORT=8080

# start server
CMD ["./server"]
