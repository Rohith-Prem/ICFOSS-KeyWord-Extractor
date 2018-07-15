from subprocess import Popen
import subprocess
import scrap
from Tokenise import tokenise
from time import sleep
from POSTagging import POStagger
from POSTagging import split_tagged
from Features import feature_extraction
from Extraction import predict
from Extraction import extraction


link = "http://www.mathrubhumi.com/news/india/cong-is-a-party-for-muslim-men-modi-1.2970970"
ret = scrap.scrapper(link)
sleep(3)
while ret:
    wordcount = tokenise.tokenizer()
    sleep(3)
    POStagger.postagger()
    sleep(3)
    split_tagged.splitTagged()
    sleep(3)
    dic = feature_extraction.featureExtractor(wordcount)
    sleep(3)
    predict.predict()
    sleep(3)
    extraction.extraction(dic)
    ret = 0



