#!/bin/bash
#kw_extractor,newmodel,newcrf,testmodel

cd /home/rohith/ICFOSS-KeyWord-Extractor/Features
cp features.txt /home/rohith/ICFOSS-KeyWord-Extractor/CRF
cd /home/rohith/ICFOSS-KeyWord-Extractor/CRF
crf_test -m kwnew features.txt > output.txt
cp output.txt /home/rohith/ICFOSS-KeyWord-Extractor/Extraction
