from subprocess import Popen
from scrap import scrapper
from Tokenise.tokenise import tokenizer
from xvfbwrapper import Xvfb
from time import sleep
from POStagger import postagger
from split_tagged import splitTagged
from feature_extraction import featureExtractor
from predict import predict
from extraction import extraction


link = "http://www.mathrubhumi.com/news/world/thai-cave-rescue-12-boys-and-coach-rescued-after-historical-ordeal-1.2959342"
ret = 0
ret = scrapper(link)
while ret:
    wordcount = tokenizer()
    ret = 0
postagger()
splitTagged()
dic = featureExtractor(wordcount)
predict()
extraction(dic)





