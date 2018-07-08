#!/usr/bin/python

from irtokz.indic_tokenize import tokenize_ind
# noinspection PyUnresolvedReferences
from sandhisplitter import Sandhisplitter

inp_file = open("scrapped_text.txt", "r", encoding="utf-8").read()
out_path = "E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\POSTagging\\tokenized_text.txt"
out_file = open(out_path, "w", encoding="utf-8")
wordcount = open("E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Features\\wordcount.txt", 'w')
language = "mal"
tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
text = tok.tokenize(inp_file)
#print(text)

#tokenizing to words
words = text.split()
#print(words)
tokens = [tk for tk in words if tk not in [".", ",", "'"]]
number_of_words = len(tokens)
print(number_of_words)

#sandhi splitting
#tokens = []
#s = Sandhisplitter()
#for w in tks:
#    split = s.split(w)
#    tokens.append(split[0])

#print(tokens)
for t in tokens:
    out_file.write("%s\n" % t)
wordcount.write("%s\n" % str(number_of_words))

out_file.close()
wordcount.close()
