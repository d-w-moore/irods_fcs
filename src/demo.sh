#!/bin/bash

DIR=$(realpath -s "$(dirname "$0")")

if [ "$1" = "" ]; then
	echo >&2 "usage: $0 [local FCS Filename] "
	exit 1
else
	fcs_file="$1"
	shift
fi

read -p 'enter keywords > ' keywords

exec "$DIR"/demo.py "$fcs_file" \
                    $keywords
