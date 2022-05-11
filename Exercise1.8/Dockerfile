# Start from the ubuntu image
FROM ubuntu:20.04

# Use /usr/src/app as our workdir. The following instructios will be executed in this location.
WORKDIR /usr/src/app

# Copy the hello.sh file from this location to /usr/src/app/
COPY getcontent.sh .

# Give run rights to the script
RUN chmod u+x ./getcontent.sh

# install curl
RUN apt update
RUN apt-get -y upgrade
RUN apt -y install curl

# When running docker run the command will be ./hello.sh
CMD ./getcontent.sh

