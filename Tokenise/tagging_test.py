from irtokz.indic_tokenize import tokenize_ind
import re
#from sandhisplitter import Sandhisplitter

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

#sandhi = Sandhisplitter()
#stem_words = []
#for t in tokens:
#    split_words = sandhi.split(t[0])
#    stem = split_words[0]
#    stem_words.append(stem)

tag = ['NNN', 'NNNP', 'NNST'] #nnn-1 nnnp-2 nnnst-3
nouns = dict()
id = 0
for t in tokens:
    if t[1] in tag and len(t[0])>2:
        nouns.setdefault(id, []).append(t[0])
        if t[1] == "NNN":
            nouns.setdefault(id, []).append(1)
        elif t[1] == "NNNP":
            nouns.setdefault(id, []).append(2)
        else:
            nouns.setdefault(id, []).append(3)
        id += 1
print(nouns)

count = 0
for i in nouns.keys():
    values = nouns[i]
    check = values[0]
    re.compile(check, re.UNICODE)
    for j in nouns.values():
        match = check.match(j[0].decode('utf-8'))
        count =






