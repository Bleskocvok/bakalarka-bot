#!/bin/bash

size="$1"

mkdir graphs &> /dev/null
cd graphs && rm -f * && cd ..

# uses http://www.graphdrawing.org/data.html
# downloaded from http://www.graphdrawing.org/download/DAGmar.tgz
java -jar DAGmar.jar multi -n "$size" -d "1.4" -i "1 to 100" -flat -c -f "graph" graphs/

for i in graphs/*; do
    # a Graphviz utility
    graphml2gv "$i" -o"$i".gv
done

cd graphs && rm -f *.graphml && cd ..

