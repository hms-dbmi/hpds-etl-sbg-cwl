# Docker image to convert `VCF` files into HPDS

This repository allows the creation of a dedicated Docker image to process `VCF` files and convert them into High Performance Data Store ([HPDS](https://github.com/hms-dbmi/pic-sure-hpds)) format. For practical purposes, the **VCFLocalLoader** option from HPDS is used as default.

This container includes the following functionalities:

* HPDS Loader
* Python3.7
* Bcftools and HTSlib

Image available in dockerhub at [dbmi/hpds-etl-sbg-cwl](https://hub.docker.com/r/dbmi/hpds-etl-sbg-cwl).

### Usage

The `entrypoint.sh` script is the core element to execute all the necessary steps to process the `VCF` files.

The `create_vcfIndex.py` script generates the necessary `vcfIndex.tsv` file so HPDS can map between the sample IDs (in the `VCF` file) and the patient IDs (the corresponding phenotypic record in PIC-SURE). 

For details on how to execute the HPDS loader tool, see the example repo [pic-sure-hpds-genotype-load-example](https://github.com/hms-dbmi/pic-sure-hpds-genotype-load-example).

### This is an effort of the [BioData Catalyst](https://www.nhlbidatastage.org/) project.

Additional references:

[PIC-SURE](https://biodatacatalyst.integration.hms.harvard.edu/psamaui/login/?redirection_url=/picsureui/)

[Seven-Briges](https://urldefense.proofpoint.com/v2/url?u=https-3A__platform.sb.biodatacatalyst.nhlbi.nih.gov_&d=DwMFaQ&c=WO-RGvefibhHBZq3fL85hQ&r=kMuQjynf327VDraj8_Yqjuir4ThBJbDsPjIwxtdpWaA&m=2Te8BSO1QfvnxmzMY9kgbYTVPtZQQdBiCAw_jcBiK2I&s=Ak33xY-cmojsC4p5MH8x-w3EKOF1hvg0KZldyefsipA&e=)
