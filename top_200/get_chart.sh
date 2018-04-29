a="https://spotifycharts.com/regional/us/daily/"
b="/download"

for i in $(cat dates.txt)
do
    echo $a$i$b
    wget -O $i $a$i$b

done
