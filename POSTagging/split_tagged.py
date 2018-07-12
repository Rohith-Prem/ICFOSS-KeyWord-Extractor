from irtokz.indic_tokenize import tokenize_ind
import re

in_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tagged_text.txt", "r", encoding="utf-8").read()
out_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/Features/tagged_split.txt", "w", encoding="utf-8")
#test_file = open("test.txt", "w", encoding="utf-8")

language = "mal"
tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
text = tok.tokenize(in_file)
print(text)
out_file.write("%s" % text)










