#!/bin/sh

if [ "$1" == ""  ]; then
  echo "wrk-pipeline.sh url [connections]"
  exit 1
fi

url = $1

if [ "$2" == "" ]; then
  connections = 256
else
  connections = $2;
fi

wrk \
  -H 'Host: localhost' \
  -H 'Accept: text/plain,text/html;q=0.9,application/xhtml+xml;q=0.9,application/xml;q=0.8,*/*;q=0.7' \
  -H 'Connection: keep-alive' \
  --latency \
  -d 15 \
  -c $connections \
  --timeout 8 \
  -t 32 \
  $url \
  -s ~/pipeline.lua \
  -- 16
