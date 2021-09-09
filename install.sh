#!/bin/sh -e

while IFS=$'\n' read -r pkg
do
    if [ -z "$pkg" ]
    then
        continue
    fi

    echo installing [$pkg]
    python -m pip install $pkg
done < requirements.txt

