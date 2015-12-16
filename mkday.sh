#!/bin/bash
if [ -z $1 ]; then
    echo 'Usage: $0 <day>'
    exit 1
fi
DAY=$(printf 'day%02d' $1)
if [ -d $DAY ]; then
    echo 'already exists'
    exit 1
fi
mkdir -p $DAY
cp template.py $DAY/part1.py
cp template.py $DAY/part2.py
cp go.sh $DAY
python get_input.py $1 $1
