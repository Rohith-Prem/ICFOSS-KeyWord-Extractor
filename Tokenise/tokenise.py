#!/usr/bin/python

import sys
import re
from irtokz.indic_tokenize import tokenize_ind #Tokenizer for Indian languages

inp_file = open("input.txt", "r", encoding="utf-8").read()
out_file = open("text.txt", "w", encoding="utf-8")
language = "mal"
tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
token_text = tok.tokenize(inp_file)
out_file.write(token_text)


