# Start from the ubuntu image
FROM ubuntu:20.04

# Use /usr/src/app as our workdir. The following instructios will be executed in this location.
WORKDIR /usr/src/app

# Copy the getcontent.sh dialogue script file from this location to /usr/src/app/
COPY getcontent.sh .

# Give run rights to the dialogue script
RUN chmod u+x ./getcontent.sh

# install curl
RUN apt update
RUN apt-get -y upgrade
RUN apt -y install curl

# When running a container, run the dialogue script as default.
CMD ./getcontent.sh

