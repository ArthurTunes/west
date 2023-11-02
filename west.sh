site=$1
for i in {1..20}; do curl -s -I -X GET $site/?author=$i | grep "location" | cut -d "/" -f6; done | tee users.txt
python wp.py $site | tee users.txt
