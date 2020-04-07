#!/bin/bash

# strip out annotations and stuff

# strip FORMAT down to GT only writing to /opt/local/hpds/vcfInput/input.vcf

mkdir -p /opt/local/hpds/vcfInput

# create vcfIndex.tsv in /opt/local/hpds pointing to /opt/local/hpds/vcfInput/input.vcf

# run HPDS variant loader
# if needed export HEAPSIZE=XXXXXX where XXXXXX is the number of MB of RAM to make available
cd /
java -Xmx${HEAPSIZE:-2048}m -jar UnifiedVCFLocalLoader-jar-with-dependencies.jar 

# compress output of HPDS loader
cd /opt/local/hpds/all
tar -xvzf /hpds_variant_data.tar.gz *


