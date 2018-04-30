#Download all available dates from the spotify charts site by iterating through the dates stored in dates.txt

a="https://spotifycharts.com/regional/us/daily/"
b="/download"

for i in $(cat datess.txt)
do
    echo $a$i$b
    wget -O "data/"$i".txt" $a$i$b

done
