#!/bin/bash

YEAR=$1
DAY=$2

if [ -z "$YEAR" ] || [ -z "$DAY" ]; then
    echo "Usage: ./get_input.sh <year> <day>"
    exit 1
fi

echo "Getting input for day $DAY of year $YEAR"

curl http://aoc-input.csornyei.com.s3.eu-central-1.amazonaws.com/$YEAR/$DAY.txt -o input.txt
