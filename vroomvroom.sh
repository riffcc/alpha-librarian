ulimit -n 4096
cd /opt/radio/ingest/
files=(*.txt)
for i in ${files[*]}; do
  parallel -j 256 -a $i wget -c -x --directory-prefix=/opt/radio/collections/$(basename $i .txt) >> /opt/radio/ingest-$(date +%Y%m%d_%H%M%S).log 2>&1
done