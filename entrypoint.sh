#!/bin/bash

# strip out annotations and stuff
# strip FORMAT down to GT only writing to /opt/local/hpds/vcfInput/input.vcf
# create vcfIndex.tsv in /opt/local/hpds pointing to /opt/local/hpds/vcfInput/input.vcf
# run HPDS variant loader
# if needed export HEAPSIZE=XXXXXX where XXXXXX is the number of MB of RAM to make available

# This Python script addesses all the above
python3 configureHPDS.py --input myfile.vcf.gz --mapping myMappingFile.csv

# Run Docker composer 
docker-compose -f $HOME/pic-sure-hpds/docker/pic-sure-hpds-etl/docker-compose-variant-loader.yml up -d

# Compress output of HPDS loader
cd /opt/local/hpds/all
tar -cvzf /hpds_variant_data.tar.gz *


