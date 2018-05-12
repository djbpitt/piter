#!/bin/bash
python concord.py \
    | grep -v 'Display' \
    | sed 's/питер/ПИТЕР/g' \
    | sed 's/петербург/ПЕТЕРБУРГ/g' \
    | sed 's/ленинград/ЛЕНИНГРАД/g'
