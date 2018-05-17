#path you want enter below
path=/home/user

source activate tensorflow
python $path/arrange.py
for url in `cat $path/Urls.log`; do
        youtube-dl -o $path'/DataSet/%(id)s.%(ext)s'  $url
done
lines=`cat Ids.log | wc - l`
echo $lines were downloaded
source deactivate
