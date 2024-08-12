ARG branch=latest
FROM cccs/assemblyline-v4-service-base:$branch

# Python path to the service class from your service directory
ENV SERVICE_PATH diec.Diec

# Install any service dependencies here
RUN apt-get -y update
RUN apt-get install -y wget
RUN wget https://github.com/horsicq/DIE-engine/releases/download/3.09/die_3.09_Ubuntu_20.04_amd64.deb -O diec.deb
RUN dpkg -i diec.deb || true
RUN apt-get -f -y install

# Copy service code
WORKDIR /opt/al_service
COPY . .

# Patch version in manifest
ARG version=4.2.0.dev1
USER root
RUN sed -i -e "s/\$SERVICE_TAG/$version/g" service_manifest.yml

# Switch to assemblyline user
USER assemblyline
