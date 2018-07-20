#!/bin/bash

cp tokenized_text.txt /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT
cd /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT
./tnt newmodel tokenized_text.txt > /home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tagged_text.txt
