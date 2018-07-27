#!/bin/bash
#largest is the latest model
cp /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tokenized_text.txt /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT
cd /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT
./tnt postagger tokenized_text.txt > /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tagged_text.txt
