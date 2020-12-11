#!/bin/bash
i=1
while IFS='' read -r line || [[ -n "$line" ]]; do
    a=${line%???????}".txt"
    if [ "$i" -lt 10 ]; then
       filename="00"$i".txt"
    elif [ "$i" -lt 100 ]; then
       filename="0"$i".txt"
    else
      filename=$i".txt"
    fi
    mv "$filename" "$a"
    echo "$i :: File renamed from $filename to $a"
    let i=i+1
done < "$1"
