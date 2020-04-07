FROM dbmi/pic-sure-hpds-etl:master_9fd46eb

RUN apt-get update -y && apt-get install -y gnupg openssl git build-essential 
RUN apt-get install -y python3-dev zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev python3-pip && rm -rf /var/lib/apt/lists/*

COPY bcftools_install.sh bcftools_install.sh
RUN bash bcftools_install.sh

RUN pip3 install pandas numpy


ENTRYPOINT "/bin/bash"
