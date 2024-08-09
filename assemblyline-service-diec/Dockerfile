FROM cccs/assemblyline-v4-service-base:latest

# Python path to the service class from your service directory
ENV SERVICE_PATH diec.Diec

# Copy Sample service code
WORKDIR /opt/al_service
COPY . .

USER root
# Install any service dependencies here
RUN apt-get -y update
RUN apt-get install -y wget
RUN wget https://github.com/horsicq/DIE-engine/releases/download/3.09/die_3.09_Ubuntu_20.04_amd64.deb -O diec.deb
RUN dpkg -i diec.deb || true
RUN apt-get -f -y install
# Patch version in manifest
ARG version=4.2.0.dev1
#RUN sed -i -e "s/\$SERVICE_TAG/$version/g" service_manifest.yml

USER assemblyline
