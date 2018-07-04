#!/usr/bin/python

from irtokz.indic_tokenize import tokenize_ind

inp_file = open("input.txt", "r", encoding="utf-8").read()
out_file = open("output.txt", "w", encoding="utf-8")
language = "mal"
tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
text = tok.tokenize(inp_file)
words = text.split()
tokens = [tk for tk in words if tk != '.']
print(tokens)
for t in tokens:
    out_file.write("%s\n" % t)
