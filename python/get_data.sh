#!/bin/bash

# downloads all available actual historic load datasets from NYISO
wget -nd -P data/ -r -l 1 -A zip http://mis.nyiso.com/public/P-58Clist.htm
unzip data/\*.zip -d data/
rm -rf data/*.zip