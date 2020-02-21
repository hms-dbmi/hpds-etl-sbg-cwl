echo "export PATH=$PATH:/usr/share/htslib:/usr/share/bcftools"  >> ~/.bashrc 
source ~/.bashrc

cd /usr/share
git clone git://github.com/samtools/htslib.git
cd htslib
make
ln -s /usr/local/bin/bin/tabix /usr/bin/tabix
ln -s /usr/local/bin/bin/bgzip /usr/bin/bgzip
make prefix=/usr/local/bin install
cd /usr/share
git clone git://github.com/samtools/bcftools.git
cd bcftools 
autoheader && autoconf && ./configure --enable-libgsl --enable-perl-filters
make 
make prefix=/usr/local/bin install # https://gist.github.com/adefelicibus/f6fd06df1b4bb104ceeaccdd7325b856
ln -s /usr/local/bin/bin/bcftools /usr/bin/bcftools
echo "export BCFTOOLS_PLUGINS=/usr/share/bcftools/plugins" >> ~/.bashrc 

