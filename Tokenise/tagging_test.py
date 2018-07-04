from irtokz.indic_tokenize import tokenize_ind
import numpy as np
from sandhisplitter import Sandhisplitter

in_file = open("tagged_text.txt", "r", encoding="utf-8").read()
out_file = open("tagged_split.txt", "w", encoding="utf-8")
#test_file = open("test.txt", "w", encoding="utf-8")

language = "mal"
tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
text = tok.tokenize(in_file)
#test_file.write(text)
words = text.split()
tokens = [tk.split('\\') for tk in words if tk != '.']
#print(tokens)
for t in tokens:
    out_file.write("%s\n" % t)

s = Sandhisplitter()

for t in tokens:
    split_words = s.split(t[0])

