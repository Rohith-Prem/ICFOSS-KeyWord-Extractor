#!/usr/bin/python

from Tokenise.irtokz.indic_tokenize import tokenize_ind
# noinspection PyUnresolvedReferences
from sandhisplitter import Sandhisplitter


def main():
    inp_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/Tokenise/scrapped_text.txt", "r", encoding="utf-8").read()
    out_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tokenized_text.txt", "w", encoding="utf-8")
    language = "mal"
    tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
    text = tok.tokenize(inp_file)
    #print(text)

    #tokenizing to words
    words = text.split()
    tokens = [tk for tk in words if tk not in [".", ",", "'"]]
    #print(tokens)

    #sandhi splitting
    tks = []
    s = Sandhisplitter()
    for w in tokens:
        split = s.split(w)
        #print(split)
        if len(split) == 2:
            if len(split[0]) <= 3:
                tks.append(split[0] + split[1])
            else:
                tks.append(split[0])
        elif len(split) == 3:
            wd = split[0] + split[1]
            tks.append(wd)
        elif len(split) == 1:
            tks.append(split[0])
    #print(tks)

    #print to output files
    for t in tks:
        out_file.write("%s\n" % t)

    number_of_words = len(tks)
    return number_of_words

def tokenizer():
    wc = main()
    return wc

#if __name__ == '__main__':
#    main()

