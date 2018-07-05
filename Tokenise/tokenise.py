#!/usr/bin/python

from irtokz.indic_tokenize import tokenize_ind

inp_file = open("scrapped_text.utf8", "r", encoding="utf-8").read()
out_path = "E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\POSTagging\\tokenized_text.txt"
out_file = open(out_path, "w", encoding="utf-8")
language = "mal"
tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
text = tok.tokenize(inp_file)
words = text.split()
tokens = [tk for tk in words if tk not in ['.', ',']]
print(tokens)
for t in tokens:
    out_file.write("%s\n" % t)
