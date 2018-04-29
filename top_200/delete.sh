
echo "prefix: "
read a

echo "range: "
read b

echo $a
rm $a

for i in $(seq 1 $b)
do
	echo $a$i
	rm $a"."$i
done
