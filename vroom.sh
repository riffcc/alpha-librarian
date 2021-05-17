ulimit -n 4096
cd /opt/radio/ingest/
files=(capscav.txt)
for i in ${files[*]}; do
  parallel -j 256 -a $i wget -c -x --directory-prefix=/opt/radio/logs/collections/$(basename $i .txt) 2>&1 | grep -i "failed\|error"
done
