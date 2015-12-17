#!/bin/sh
if [ -f part1.py ]; then
    echo '--- PART 1 ---'
    PYTHONPATH=.. python part1.py $@
fi
if [ -f part2.py ]; then
    echo '--- PART 2 ---'
    PYTHONPATH=.. python part2.py $@
fi
