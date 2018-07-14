#!/bin/bash

cp /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tokenized_text.txt /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT
cd /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT
./tnt train tokenized_text.txt > /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tagged_text.txt
