# Change to your config path
CONFIG_PATH=./config/steno_crawl.yml

SEARCH="  - url: .*"
REPLACE="  - url: ${1}"

sed -i -e "s@$SEARCH@$REPLACE@g" $CONFIG_PATH

docker cp $CONFIG_PATH crawler:app/config/crawler.yml

docker exec -it crawler bin/crawler crawl ./config/crawler.yml