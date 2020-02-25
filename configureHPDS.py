#!/usr/bin/python3
import argparse
import os
import pandas as pd

stream = os.popen("free -m | grep Mem | awk '{print $2}'").read().replace('\n','')
RAM = int(stream)

parser = argparse.ArgumentParser(description='Script to execute VCF to HPDS conversion', 
								prog='python3 runHPDS.py')
# Input VCF
parser.add_argument('--input', '-i', required=True,
					type=str,
					help='Path to the input VCF file')
# Patient Mapping file 
parser.add_argument('--mapping', '-m', required=True,
					type=str,
					help='Path to the patient mapping file')
# Specify memory 
parser.add_argument('--heap', '-s', 
					default=RAM, type=int,
					help='Total memory (MB) allowed for the HEAPSIZE to use. Default: uses all the system memory')
args = parser.parse_args()


print("\nInput VCF file: " + str(args.input))
print("\nPatient mapping file: " + str(args.mapping))
print("\nThe HEAP will use: "+str(args.heap)+" MB of memory")

os.system("""echo "version: '3.3'
services:
  variant-loader:
    image: dbmi/pic-sure-hpds-etl:master_d1da0b6
    environment:
      - HEAPSIZE="""+str(args.heap)+"""
      - LOADER_NAME=VCFLocalLoader
    volumes:
      - ./hpds:/opt/local/hpds
      - ./vcfLoad:/opt/local/hpds/vcfInput
      - ./hpds/all:/opt/local/hpds/vcfOutput" >  $HOME/pic-sure-hpds/docker/pic-sure-hpds-etl/docker-compose-variant-loader.yml""")


os.system('cd $HOME && git clone https://github.com/hms-dbmi/pic-sure-hpds.git')
os.system('mkdir pic-sure-hpds/docker/pic-sure-hpds-etl/vcfLoad')
os.system('cp '+args.input+' pic-sure-hpds/docker/pic-sure-hpds-etl/vcfLoad/')
os.system('mkdir ~/patientMappings/')
os.system('cp '+args.mapping+' ~/patientMappings/')

# Create vcfIndex.tsv
print("Creating vcfIndex.tsv file")

# # Patient mapping file sample: 
# "41820","Dataset_Name","1500"
# "41720","Dataset_Name","1609"
# "21720","Dataset_Name","1506"
# "61520","Dataset_Name","1605"


os.system('bcftools query -l '+args.input+' | awk \'{ print "\\""$0"\\""}\' > $HOME/patientMappings/VCF_sample_ids.txt')
inFile1 = pd.read_csv("$HOME/patientMappings/VCF_sample_ids.txt", names=["samples"], dtype=str)
inFile2 = pd.read_csv("$HOME/patientMappings/"+args.mapping, names=["samples", "dataSet", "patients"], dtype=str)
match=pd.merge(inFile1, inFile2, on=["samples"], how='inner')
samples=match['samples'].str.cat(sep=",")
patients=match['patients'].str.cat(sep=",")
# Configuration file structure:
data={'filename': ['/opt/local/hpds/vcfInput/'+args.input],'chromosome': ['ALL'] ,'annotated': [1] ,'gzip': [1] ,'sample_ids': [samples] ,'patient_ids': [patients],'sample_relationship': [''] ,'related_sample_ids': ['']} 
df = pd.DataFrame(data)
# Save vcfIndex
df.to_csv(path_or_buf='$HOME/pic-sure-hpds/docker/pic-sure-hpds-etl/hpds/vcfIndex.tsv', sep='\t',header=True, index=False)
